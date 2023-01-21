from fastapi import APIRouter
from app.endpoints import menus, submenus, dishes


router = APIRouter()
router.include_router(menus.router)
router.include_router(submenus.router)
router.include_router(dishes.router)
