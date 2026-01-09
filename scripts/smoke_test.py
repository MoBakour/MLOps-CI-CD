import time
import sys
import requests

BASE_URL = "http://127.0.0.1:8000"


def wait_for_health(timeout_seconds: int = 20) -> None:
    start = time.time()
    while time.time() - start < timeout_seconds:
        try:
            r = requests.get(f"{BASE_URL}/health", timeout=2)
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError("Service did not become healthy in time")


def main() -> int:
    wait_for_health()

    r = requests.post(
        f"{BASE_URL}/predict",
        json={"user_id": "smoke_user", "num_buckets": 10},
        timeout=5,
    )
    if r.status_code != 200:
        print("Smoke test failed:", r.status_code, r.text)
        return 1

    print("Smoke test passed:", r.json())
    return 0


if __name__ == "__main__":
    sys.exit(main())
