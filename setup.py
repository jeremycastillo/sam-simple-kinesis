from setuptools import setup, find_packages

setup(
    name="simple_kinesis",
    packages=find_packages('src/simple_kinesis'),
    package_dir={'': 'src'}
)