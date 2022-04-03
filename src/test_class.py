# content of test_class.py
try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
