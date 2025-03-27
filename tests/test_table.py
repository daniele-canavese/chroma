"""Tests for the progress bars."""

from time import sleep

from _pytest.capture import CaptureFixture

from chroma import Level, ProgressBar, Table, pprint


def test_table(capsys: CaptureFixture) -> None:
    """
    Test the tables.
    :param capsys: the capture fixture
    """
    # A simple table with three columns.
    table = Table("one", "two", "three")
    table.add(1, 2, 3)
    pprint(table)
    assert capsys.readouterr().out != ""
