"""{{cookiecutter.project_slug}}"""
from {{ cookiecutter.project_slug }} import logger

def main():
    """Main Entry point for {{cookiecutter.project_name}}"""
    log = logger.setup_logger("{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.log")


if __name__ == '__main__':
    main()
