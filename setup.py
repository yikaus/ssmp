from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ssmp',
    version='0.0.1',
    description='CLI tool on AWS SSM parameter',
    long_description=readme,
    author='Kevin Yi',
    author_email='yikaus at gmail.com',
    url='https://github.com/yikaus/ssmp',
    scripts=['ssmp/main.py'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points = {
        'console_scripts': [
            'ssmp = ssmp.main:ssm',
        ],
    }
)
