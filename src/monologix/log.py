import functools
import logging
from collections.abc import Callable
from typing import ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def log_monad(
    error_message: str,
    warn_on_error: bool = False,
    logger: logging.Logger = logging.getLogger(__name__),
    info_on_error: bool = False,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    log_monad is a decorator that wraps a function and add logging capabilities to it.

    params:
    error_message: str: The message to log when an error occurs.
    warn_on_error: bool: If True, logs a warning when an error occurs.
    logger: logging.Logger: The logger to use. Default is the logger of the module.
    info_on_error: bool: If True, logs an info message when an error occurs.
    handleError: Callable[[Exception], None]: A function to handle the error. Default is a function that does nothing.
    """

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        functools.wraps(func)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            logger.info(f"Running {func.__name__}")
            try:
                result = func(*args, **kwargs)
            except Exception as e:  # pylint: disable=broad-except
                logger.error(f"{error_message}: {e}")
                if warn_on_error:
                    logger.warning(f"{func.__name__} failed")
                if info_on_error:
                    logger.info(f"{func.__name__} failed")
                raise

            logger.info(f"{func.__name__} returned: {result}")
            return result

        return wrapper

    return decorator
