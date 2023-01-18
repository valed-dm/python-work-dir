from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any


from app import deps
from app.crud import crud_menus as crud
from app.schemas.menus import Menus, MenusCreate, MenusUpdate


# APIRouter creates path operations for menus module
router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menus"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=200)
def get_all_menus_items(
    request: Request,
    db: Session = Depends(deps.get_db),
):
    """
    READ all menus items
    """
    return crud.menus.get_multi(db=db, limit=100)


@router.get("/{menu_id}", status_code=200)
def fetch_menus_item(
    *,
    menu_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    READ a single menu item
    """
    result = crud.menus.get(db=db, id=menu_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Menu item with ID {menu_id} not found"
        )

    return result


@router.post("/", status_code=201)
def add_menus_item(
    *, menu_item_in: MenusCreate, db: Session = Depends(deps.get_db)
):
    """
    CREATE a new menu item.
    """
    return crud.menus.create(db=db, obj_in=menu_item_in)


@router.delete("/{menu_id}", status_code=200)
def delete_menus_item(
    *, menu_id: int, db: Session = Depends(deps.get_db)
):
    """
    DELETE a menu item.
    """
    return crud.menus.remove(db=db, id=menu_id)


@router.patch("/{menu_id}}", status_code=201)
def update_menus_item(
    *, menu_id, updated_fields: MenusUpdate, db: Session = Depends(deps.get_db)
):
    """
    UPDATE a menu item.
    """
    return crud.menus.update_item(db=db, item_id=menu_id, updated_fields=updated_fields)
