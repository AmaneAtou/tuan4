from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/get_version")
async def get_version():
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
async def check_prime(number: int):
    if number <= 1:
        return {"is_prime": False}
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

