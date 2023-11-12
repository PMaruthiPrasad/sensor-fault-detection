from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """ 
    this function will return list of requiremnst 
    """
    # Assignment-1 

    """
    write code to read requiremnts.txt file and append requirements in requirmeent_list variable 
    """
    requirement_list:List[str] = []
    return requirement_list 

setup (
    name='sensor',
    version='0.0.1',
    author='Maruthi',
    author_email='pmaruthiprasad16@gmail.com',
    packages=find_packages(),
    install_requires=[],

)
