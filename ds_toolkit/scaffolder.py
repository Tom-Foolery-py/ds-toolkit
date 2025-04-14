import os 
from pathlib import Path 

def scaffold_project(project_path: Path, use_git: bool = True, use_notebook: bool = True):
    """
    Creates the folder structure and starter files for a new data science project.
    
    Args:
        project_name (str): The name of the new project.
        use_git (bool): Whether to initialize a git repository. Defaults to True.
        use_notebook (bool): Whether to create a Jupyter notebooks folder. Defaults to True.
    """
    print(f"Creating project directory at {project_path}...")
    
    # Create project directory
    try: 
        project_path.mkdir(exist_ok=False)
    except FileExistsError:
        print(f"Directory {project_path} already exists. Please choose a different project name.")
        return
    except OSError as e:    
        print(f"Error creating directory {project_path}: {e}")
        return
    print(f"Project directory {project_path} created successfully.")
    
    # Create subdirectories
    subdirs = ["data", "src", "tests"]
    if use_notebook:
        subdirs.append("notebooks")
    
    for subdir in subdirs:
        (project_path / subdir).mkdir()
        print(f"Subdirectory {subdir} created successfully.")
        
    # Create README file
    readme_path = project_path / "README.md"
    readme_path.write_text(f"# {project_path}\n\n## Project Overview\n\n")
    print(f"README file created at {readme_path}.")
        
    print("Project scaffolded successfully!")
    
    