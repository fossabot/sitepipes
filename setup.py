from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='sitepipes',
    version='0.0.1',
    description='A framework for federated learning applications',
    long_description=long_description,
    license=license,
    author='Eric Yates',
    author_email='eric@medleyagency.com',
    url='https://github.com/MedleyLabs/sitepipes',
    packages=['sitepipes'],
)

