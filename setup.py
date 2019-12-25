from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ssmp',
    version='0.0.4',
    description='CLI tool for AWS SSM parameter',
    long_description_content_type='text/markdown',
    long_description=readme,
    author='Kevin Yi',
    author_email='yikaus@gmail.com',
    url='https://github.com/yikaus/ssmp',
    scripts=['ssmp/main.py'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'click',
        'boto3',
        'pandas',
    ],
    entry_points = {
        'console_scripts': [
            'ssmp = ssmp.main:ssm',
        ],
    }
)
