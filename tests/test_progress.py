"""Tests for the progress bars."""

from time import sleep

from _pytest.capture import CaptureFixture

from chroma import Level, ProgressBar, pprint


def test_progress(capsys: CaptureFixture) -> None:
    """
    Test the progress bars.
    :param capsys: the capture fixture
    """
    for _ in ProgressBar(range(1000)):
        sleep(0.001)
    assert capsys.readouterr().out != ""
