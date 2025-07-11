# context_logger

* A Python package to efficiently log an event's start time, end time and elapsed time period using loguru and ContextManager.

## How to install

```pip install git+https://github.com/knowru/context_logger.git```

## Without context_logger

```python
import time
from datetime import datetime


def run(*args, **kwargs):
    some_id = kwargs.get("some_id")
    logs = []

    start_time = datetime.now()
    print(f"{start_time} Started calling API 1")
    logs.append(f"{start_time} Started calling API 1")
    time.sleep(1)
    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds() * 1000
    print(f"{end_time} Finished calling API 1 ({elapsed=:.2f}ms)")
    logs.append(f"{end_time} Finished calling API 1 ({elapsed=:.2f}ms)")

    return {"some_id": some_id, "logs": logs}

if __name__ == "__main__":
    run(some_id=123)
```

### Output

```
2025-07-11 14:11:12.155671 Started calling API 1
2025-07-11 14:11:13.155985 Finished calling API 1 (elapsed=1000.31ms)
```

## With context_logger

```python
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


def run(*args, **kwargs):
    some_id = kwargs.get("some_id")
    logger = global_logger.bind(some_id=some_id)
    clf = ContextLoggerFactory(logger)

    with clf("calling API 1"):
        time.sleep(1)

    return {"some_id": some_id}


if __name__ == "__main__":
    run(some_id=123)
```

### Output

```
2025-07-11 14:11:51.238 +09:00 | DEBUG    | context_logger.context_logger:__enter__:35 | some_id=123 |  Started calling API 1 @ __main__.run:21
2025-07-11 14:11:52.240 +09:00 | DEBUG    | context_logger.context_logger:__exit__:41 | some_id=123 |  Finished calling API 1 @ __main__.run:21 (elapsed: 1001.33 ms)
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License.

- Free for non-commercial use.
- Commercial use requires a separate paid license. Please contact spark@knowru.com for details.
