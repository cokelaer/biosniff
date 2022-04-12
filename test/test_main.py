from biosniff.main import sniffer


from . import test_dir

def test_main():

    from click.testing import CliRunner
    runner = CliRunner()

    # fastq command
    filename1 = f"{test_dir}/../../data/fastq/test.fastq.gz"
    results = runner.invoke(sniffer, ['--help'])
    assert results.exit_code == 0
    results = runner.invoke(sniffer, [f"{test_dir}/data/measles.sam"])
    assert results.exit_code == 0


