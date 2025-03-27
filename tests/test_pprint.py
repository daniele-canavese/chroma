"""Tests for `pprint`."""

from _pytest.capture import CaptureFixture

from chroma import Level, pprint


def test_pprint(capsys: CaptureFixture) -> None:
    """
    Test the `pprint` function.
    :param capsys: the capture fixture
    """
    # Print some normal text.
    pprint("test")
    assert capsys.readouterr().out == "test\n"

    # Print some colored text.
    pprint("42", highlight=True)
    assert capsys.readouterr().out == "42\n"
