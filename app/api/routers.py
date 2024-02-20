from fastapi import APIRouter

from app.api.device import router as device_router
from app.api.data import router as data_router
from app.api.analyze import router as analyze_router


main_router = APIRouter()
main_router.include_router(
    device_router, prefix='/device', tags=['Device']
)
main_router.include_router(
    data_router, prefix='/data', tags=['Data']
)
main_router.include_router(
    analyze_router, prefix='/analyze_statistics', tags=['Analyze_statistics']
)
