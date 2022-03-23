import logging
from functools import wraps

RETRIES_LIMIT = 5


class WithRetry:
    def __init__(self, retires_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retires_limit = retires_limit
        self.allowed_exceptions = allowed_exceptions

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(self.retires_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    logging.info(f"retrying! {e}")
                    last_raised = e
            raise last_raised

        return wrapped
