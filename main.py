from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class HealthCheck(BaseModel):
    
    status: str = "OK"


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a HealthCheck",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)

def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0")

if __name__ == "__main__":
    main()