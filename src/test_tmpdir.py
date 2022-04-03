# content of test_tmpdir.py
try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa


def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
