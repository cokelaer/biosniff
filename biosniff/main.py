##############################################################################
import glob
import os
from pathlib import Path
import pkg_resources
import shutil

import click

import colorlog

logger = colorlog.getLogger(__name__)


from biosniff import version

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command()
@click.version_option(version=version)
@click.argument("input", type=click.STRING)
def sniffer(**kwargs):
    """

    Infers format of the input file

        biosniff data.fa

    """
    from biosniff import Sniffer, logger

    logger.setLevel("ERROR")
    s = Sniffer()
    ret = s.sniff(kwargs["input"])
    print(ret)
