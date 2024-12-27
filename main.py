from fastapi import FastAPI
from typing import Any

app = FastAPI()

@app.get("/version")
def get_version() -> Any:
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int) -> Any:
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}
