from functools import wraps
import logging


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ConnectionError as e:
                logging.info(f"retry! {e}")
            raise last_raised

    return wrapped


@retry
def run_operation(task):
    return task.run()
