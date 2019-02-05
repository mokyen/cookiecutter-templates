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
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def version():
    with open('VERSION') as version_file:
        return version_file.read().strip()


setup(name='hyphelper',
      version=version(),
      description='Help make life easier when using Hyperlynx SI/DRC',
      long_description=readme(),
      long_description_content_type='text/x-rst',
      url='https://bitbucket.org/jdpatt/hyphelper/',
      keywords='hyperlynx drc pi si mentor cadence',
      author='David Patterson',
      packages=find_packages(exclude=['docs', 'tests*']),
      python_requires='>=3.4',
      install_requires=["Click", "openpyxl"],
      entry_points={"console_scripts": ['hyphelper = hyphelper.hyphelper:cli']},
      include_package_data=True,
      zip_safe=False)
