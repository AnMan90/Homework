import io
import os
import sys

import pytest

from src.decorators import log


def test_log_decorator(tmp_path):
    """Тест для декоратора log"""
    log_file = os.path.join(tmp_path, "test.log")

    @log(filename=log_file)
    def add(a, b):
        return a + b

    assert add(2, 3) == 5

    with open(log_file) as f:
        assert "add ok" in f.read()

    @log(filename=log_file)
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(log_file) as f:
        content = f.read()
        assert "div error: ZeroDivisionError" in content
        assert "Inputs: (1, 0)" in content

    old_stdout = sys.stdout
    sys.stdout = captured = io.StringIO()

    try:

        @log()
        def greet(name):
            return f"Hello, {name}"

        assert greet("Alice") == "Hello, Alice"
        assert "greet ok" in captured.getvalue()
    finally:
        sys.stdout = old_stdout

    old_stdout = sys.stdout
    sys.stdout = captured = io.StringIO()

    try:

        @log()
        def fail():
            raise ValueError("Test error")

        with pytest.raises(ValueError):
            fail()

        assert "fail error: ValueError" in captured.getvalue()
        assert "Inputs: ()" in captured.getvalue()
    finally:
        sys.stdout = old_stdout
