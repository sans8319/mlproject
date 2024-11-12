from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements,
    excluding '-e .' which is not a valid package specifier.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name='sanskriti',
    version='0.0.1',
    author='sanskriti',
    author_email='sanskritigupta8319@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
