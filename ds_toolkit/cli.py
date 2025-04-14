import typer
from ds_toolkit.scaffolder import scaffold_project
from ds_toolkit.env_setup import setup_env
from ds_toolkit.git_tools import init_git
from pathlib import Path

app = typer.Typer(help="DS Toolkit: Quickly scaffold data science projects.")

@app.command()
def init(
    project_name: str = typer.Argument(..., help="Name of your new project"),
    use_git: bool = typer.Option(True, "--git/--no-git", help="Initialize a git repository"),
    use_venv: bool = typer.Option(True, "--venv/--no-venv", help="Create a virtual environment"),
    use_notebook: bool = typer.Option(True, "--notebook/--no-notebook", help="Create a Jupyter notebooks folder")
):
    """
    Initializes a new data science project.
    """
    project_path = Path(project_name)
    
    typer.echo(f"Scaffolding project: {project_path}")
    
    scaffold_project(
        project_path=project_path,
        use_git=use_git,
        use_notebook=use_notebook
    )
    
    
    
    if use_venv:
        typer.echo("Setting up virtual environment...")
        setup_env(project_path)
        
    if use_git:
        typer.echo("Initializing git repository...")
        init_git(project_path)

    typer.echo("Project setup complete! Have fun!")
    
        
if __name__ == "__main__":
    app()