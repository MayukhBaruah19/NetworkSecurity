from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]: 
    requirements_list:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.split()
                if requirements and requirements!="-e .":
                    requirements_list.append(requirements)
        
    except FileNotFoundError:
        return('requirements.txt file is not found')
    


setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Mayukh',
    author_email='mayukhbaeuah91@gmail.com',
    description='A package for predicting customer churn using machine learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MayukhBaruah19/Customer-churn-prediction',
    packages=find_packages(),
    install_requires=get_requirements() 
)    