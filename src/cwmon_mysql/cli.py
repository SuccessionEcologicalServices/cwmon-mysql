"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcwmon_mysql` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``cwmon_mysql.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``cwmon_mysql.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
from cwmon.cli import cwmon


@cwmon.group()
@click.pass_context
def mysql(ctx):
    """Group MySQL monitoring commands for ``cwmon``."""
    click.echo(repr(ctx))
