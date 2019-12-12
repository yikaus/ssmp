#!/usr/bin/env python3

import click

from . import aws

@click.group()
def ssm():
    pass

@ssm.command()
def ls():
    click.echo('ls ssm parameter')
    aws.get_ssms()

@ssm.command()
def cd():
    click.echo('go into path')


if __name__ == '__main__':
    ssm()
