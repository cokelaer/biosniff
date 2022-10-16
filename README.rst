BioSniff
############



.. figure:: https://raw.githubusercontent.com/cokelaer/biosniff/main/doc/biosniff_logo_256.png
    :alt: logo
    :align: center
    :target: https://raw.githubusercontent.com/cokelaer/biosniff/main/doc/biosniff_logo_256.png
    :width: 10%

.. image:: https://badge.fury.io/py/biosniff.svg
    :target: https://pypi.python.org/pypi/biosniff

.. image:: https://github.com/cokelaer/biosniff/actions/workflows/main.yml/badge.svg?branch=main
    :target: https://github.com/cokelaer/biosniff/actions/workflows/main.yml

.. image:: https://coveralls.io/repos/github/cokelaer/biosniff/badge.svg?branch=main
    :target: https://coveralls.io/github/cokelaer/biosniff?branch=main

:Python version: 3.7, 3.8, 3.9, 3.10
:Issues: `On github <https://github.com/cokelaer/biosniff/issues>`_


This tools is a simple Sniffer for Biological formats (and compression formats)


Installation
===============

::

    pip install biosniff

Usage
======

::

    biosniff file.fasta
    biosniff example.vcf
    ...

There are about 50 formats supported for now including: 

    abi, bam, bai, bcf, binary_bed, bed, bedgraph, bigwig, bigbed, bplink,
    bz2, cram, clustal, dsrc, embl,ena, fasta, fastq, genbank, gfa, gff2,
    gff3, gz, json, maf, newick, nexus, ods, paf, phylip, phyloxml, plink,
    qual, sam, scf, stockholm, rar, twobit, tsv, vcf, wiggle, wig, 
    xls, xlsx, xmfa, yaml, zip, 7zip, xz


Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
1.0.0     * add logo, add Python 3.10 in CI and tag to version 1.0
0.4.0     * additional test and fix missing click requirements
0.3.0     * add missing MANIFEST and applied black
0.2.0     * more tests (80% coverage) and some simplifications
0.1.0     * first commit
========= ====================================================================

