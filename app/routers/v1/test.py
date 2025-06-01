from fastapi import APIRouter, Depends

from app.dependencies.auth import validate_api_key

test_router = APIRouter(
    prefix="/test",
    responses={404: {"description": "Not found"}},
)


@test_router.get("/")
async def get_test():
    return {"message": "Hello World"}


@test_router.get("/auth")
async def get_auth(_: str = Depends(validate_api_key)):
    return {"message": "Hello World with Auth"}
