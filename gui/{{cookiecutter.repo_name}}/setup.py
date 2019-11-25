from setuptools import setup
import {{ cookiecutter.repo_name }}


def readme():
    """Open up the readme and use the text for the long description."""
    with open('README.md') as f:
        return f.read()


setup(
    name='{{ cookiecutter.repo_name }}',
    version={{ cookiecutter.repo_name }}.__version__,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme(),
    author='{{ cookiecutter.full_name }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=["Click", "PySide2",],
    license='MIT',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
