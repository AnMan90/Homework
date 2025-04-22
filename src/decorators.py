import datetime
import functools


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"[{datetime.datetime.now()}] {message}")
                else:
                    print(message, end="")
                raise

            if filename:
                with open(filename, "a") as f:
                    f.write(f"[{datetime.datetime.now()}] {message}")
            else:
                print(message, end="")

            return result

        return wrapper

    return decorator
