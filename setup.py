from setuptools import setup, find_packages

setup(
    name='cli_todo_app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'todo=cli_todo_app.main:main',
        ],
    },
)
