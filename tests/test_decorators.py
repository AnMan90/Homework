import io
import os
import sys

import pytest

from src.decorators import log


def test_log_decorator_success(tmp_path):
    """Тест успешного выполнения функции с логированием в файл"""
    log_file = os.path.join(tmp_path, "test.log")

    @log(filename=log_file)
    def add(a, b):
        return a + b

    assert add(2, 3) == 5

    with open(log_file) as f:
        assert "add ok" in f.read()


def test_log_decorator_error(tmp_path):
    """Тест обработки ошибки с логированием в файл"""
    log_file = os.path.join(tmp_path, "test.log")

    @log(filename=log_file)
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(log_file) as f:
        content = f.read()
        assert "div error: ZeroDivisionError" in content
        assert "Inputs: (1, 0)" in content


def test_log_decorator_stdout_success():
    """Тест успешного выполнения с выводом в stdout"""
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


def test_log_decorator_stdout_error():
    """Тест обработки ошибки с выводом в stdout"""
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
