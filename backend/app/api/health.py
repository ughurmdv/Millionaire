from fastapi import APIRouter
from datetime import datetime

from logger import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "OK"
}