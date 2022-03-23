import logging
from functools import wraps


class ControlledException:
    ...


RETRIES_LIMIT = 3


def with_retry(
    retires_limit=RETRIES_LIMIT,
    allowed_exceptions=None,
):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(retires_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logging.info(f"retrying! {e}")
                    last_raised = e
            raise last_raised

        return wrapped

    return retry


@with_retry()
def run_operation(task):
    return task.run()


@with_retry()
def run_with_custom_retries_limit(task):
    return task.run()


@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    return task.run()


@with_retry(retires_limit=4, allowed_exceptions=(ZeroDivisionError,))
def run_with_custom_parameters(task):
    return task.run()
