# content of test_class_demo.py
try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa


class TestClassDemoInstance:
    def test_one(self):
        assert 0

    def test_two(self):
        assert 0
