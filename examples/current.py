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

    start_time = datetime.now()
    print(f"{start_time} Started calling API 2")
    logs.append(f"{start_time} Started calling API 2")
    time.sleep(2)
    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds() * 1000
    print(f"{end_time} Started calling API 2 ({elapsed=:.2f}ms)")
    logs.append(f"{end_time} Finished calling API 2 ({elapsed=:.2f}ms)")

    return {"some_id": some_id, "logs": logs}


if __name__ == "__main__":
    run(some_id=123)
