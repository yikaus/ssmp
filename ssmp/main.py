#!/usr/bin/env python3

import click

from . import aws

@click.group()
def ssm():
    pass

@ssm.command()
@click.argument('path')
def ls(path):
    aws.get_ssms(path)

@ssm.command()
@click.option('-r','--recursive',is_flag=True)
@click.option('-v','--value',is_flag=True)
@click.argument('key')
@click.argument('path')
def grep(path,key,recursive,value):
    aws.search_ssms(path,key,recursive,value)


if __name__ == '__main__':
    ssm()
