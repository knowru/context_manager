import sys
import time
from datetime import datetime
from loguru import logger as global_logger

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

    start_time = datetime.now()
    logger.debug(f"Started calling API 1")
    time.sleep(1)
    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds() * 1000
    logger.debug(f"Finished calling API 1 ({elapsed=:.2f}ms)")

    start_time = datetime.now()
    logger.debug(f"Started calling API 2")
    time.sleep(2)
    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds() * 1000
    logger.debug(f"Finished calling API 2 ({elapsed=:.2f}ms)")

    return {"some_id": some_id}


if __name__ == "__main__":
    run(some_id=123)
