import subprocess
from pathlib import Path 

DEFAULT_GITIGNORE = """
__pycache__/
.venv/
.env/
.ipynb_checkpoints/
.DS_Store
*.pyc
*.pyo
*.pyd
.db
"""

def init_git(project_path: Path):
    """
    Initializes a git repository in the project directory and creates a default .gitignore file.
    """
    
    print(f"Initializing git repository at {project_path}...")
    
    result = subprocess.run(["git", "init"], cwd=project_path, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error initializing git repository: {result.stderr}")
        return
    
    print("Git repository initialized successfully.")
    
    gitignore_path = project_path / ".gitignore"
    if not gitignore_path.exists():
        gitignore_path.write_text(DEFAULT_GITIGNORE.strip())
        print(f".gitignore file created at {gitignore_path}.")
    else:
        print(f".gitignore file already exists at {gitignore_path}.")
        
        
        