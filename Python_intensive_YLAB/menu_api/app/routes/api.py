from fastapi import APIRouter
from app.endpoints import menus, submenus


router = APIRouter()
router.include_router(menus.router)
router.include_router(submenus.router)
