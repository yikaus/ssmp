#!/usr/bin/env python3

import click

from . import aws

@click.group()
def ssm():
    pass

@ssm.command()
@click.option('-r','--recursive',is_flag=True)
@click.option('-a','--all',is_flag=True)
@click.option('-q','--quiet',is_flag=True)
@click.argument('path')
def ls(path,recursive,all,quiet):
    aws.get_ssms(path,recursive,all,quiet)

@ssm.command()
@click.option('-r','--recursive',is_flag=True)
@click.option('-v','--value',is_flag=True)
@click.option('-a','--all',is_flag=True)
@click.option('-q','--quiet',is_flag=True)
@click.argument('key')
@click.argument('path')
def grep(path,key,recursive,value,all,quiet):
    aws.search_ssms(path,key,recursive,value,all,quiet)


if __name__ == '__main__':
    ssm()
