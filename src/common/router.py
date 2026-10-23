from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@router.get("/health")
def read_health() -> dict[str, str]:
    return {"status": "ok"}
