from fastapi import APIRouter

from .test import test_router
from .scraper import router as scraper_router

router = APIRouter()
router.include_router(test_router)
router.include_router(scraper_router)
