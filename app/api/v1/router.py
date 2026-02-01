from fastapi import APIRouter
from app.api.v1.routes import orders

router = APIRouter(prefix="/api/v1")

router.include_router(orders.router, prefix="/orders", tags=["Orders"])
