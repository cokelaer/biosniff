import os
import glob
import pytest
from . import test_dir
from biosniff import Sniffer

sharedir = f"{test_dir}/data"



def test_sniffer():
    s = Sniffer()
    assert s.sniff(f"{sharedir}/__init__.py") is None

    # now with a valid file already implemented
    assert s.sniff(f"{sharedir}/measles.fa") == "fasta"




files = [
    'measles.fa', 
    'measles.fa.fai',
    'measles_R1_.fastq.gz',
    "measles.sam",
    "measles.bam",
    "ABI/310.ab1",
    "measles.gbk",
    "test_tabulated.xls",
    "test_tabulated.xlsx",
    "test_tabulated.ods"
]

@pytest.mark.parametrize("filename", files)
def test_sniffer_all(filename):
    s = Sniffer()

    print(f"{sharedir}/{filename}")
    ret = s.sniff(f"{sharedir}/{filename}")



