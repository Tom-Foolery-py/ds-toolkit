import subprocess
import sys 
from pathlib import Path
import venv
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn

def setup_env(project_path: Path) -> None:
    
    """
    Sets up the environment for a data science project in the project folder.
    
    Args:
        project_path (str): Root project directory.
    """
    
    venv_path = Path(project_path) / ".venv"
    print(f"Creating virtual environment at {venv_path}...")
    
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_path)
    
    print(f"Virtual environment created at {venv_path}.")
    
    pip_executable = venv_path / "Scripts" / "pip" if sys.platform == "win32" else venv_path / "bin" / "pip"
    with Progress(
        BarColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("Installing starter packages...", total=None)
        subprocess.run([str(pip_executable), "install", "pandas", "numpy", "scikit-learn", "matplotlib", "seaborn"], check=True)
        progress.remove_task(task)
        
    print("Starter packages installed.")
    
    req_file_path = Path(project_path) / "requirements.txt"
    print(f"Creating requirements.txt at {req_file_path}...")
    with req_file_path.open("w") as f:
        subprocess.run([str(pip_executable), "freeze"], stdout=f)
        
    print(f"requirements.txt created at {req_file_path}.")
    print("Environment setup complete. Activate the virtual environment using:")
    print(f"source {venv_path}/bin/activate" if sys.platform != "win32" else f"{venv_path}\\Scripts\\activate")