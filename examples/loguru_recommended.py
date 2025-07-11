import sys
import time
from loguru import logger as global_logger
from context_logger import ContextLoggerFactory

global_logger.remove()
format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS Z}</green> | <level>{level: <8}</level> |"
    " <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> |"
    " some_id={extra[some_id]} |  <level>{message}</level>"
)
global_logger.add(sys.stderr, format=format)
# global_logger.add(cloudwatch_handler, format=format)


def run(*args, **kwargs):
    some_id = kwargs.get("some_id")
    logger = global_logger.bind(some_id=some_id)
    clf = ContextLoggerFactory(logger)

    with clf("calling API 1"):
        time.sleep(1)

    with clf("calling API 2"):
        time.sleep(1)

    return {"some_id": some_id}


if __name__ == "__main__":
    run(some_id=123)
