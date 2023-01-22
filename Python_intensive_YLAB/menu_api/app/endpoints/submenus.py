from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


from app import deps
from app.crud import crude_submenus as crud
from app.schemas.submenus import Submenus, SubmenusCreate, SubmenusUpdate


# APIRouter creates path operations for submenus module
router = APIRouter(
    prefix="/api/v1/menus/{api_test_menus_id}/submenus",
    tags=["Submenus"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=200)
def get_all_submenus_items(
    api_test_menus_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Submenus]:
    """
    READ all submenus items
    """
    submenus_items_list = jsonable_encoder(
        crud.submenus.get_multi(db=db, limit=100))
    return list(filter(
        lambda x: x['menus_id'] == api_test_menus_id,
        submenus_items_list
    ))


@router.get("/{api_test_submenus_id}", status_code=200)
def get_submenus_item(
    api_test_submenus_id: int,
    db: Session = Depends(deps.get_db),
):
    """
    READ a single submenus item
    """
    result = crud.submenus.get(db=db, id=api_test_submenus_id)

    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404,
            # detail=f"Submenu item with ID {api_test_submenus_id} not found"
            detail="submenu not found"
        )

    result = jsonable_encoder(result)
    result['id'] = str(result['id'])

    return result


@router.post("", status_code=201)
def add_submenus_item(
    api_test_menus_id: int,
    submenus_item_in: SubmenusCreate,
    db: Session = Depends(deps.get_db)
):
    """
    CREATE a new submenus item.
    """
    item_in: dict = jsonable_encoder(submenus_item_in)
    item_in.update({'menus_id': api_test_menus_id})

    result = crud.submenus.create(db=db, obj_in=item_in)
    result = jsonable_encoder(result)
    result['id'] = str(result['id'])

    return result


@router.delete("/{api_test_submenus_id}", status_code=200)
def delete_submenus_item(
    api_test_submenus_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    DELETE a submenus item.
    """
    return crud.submenus.remove(db=db, id=api_test_submenus_id)


@router.patch("/{api_test_submenus_id}}", status_code=200)
def update_submenus_item(
    api_test_submenus_id: int,
    updated_fields: SubmenusUpdate,
    db: Session = Depends(deps.get_db)
):
    """
    UPDATE a submenus item.
    """
    return crud.submenus.update_item(
        db=db,
        item_id=api_test_submenus_id,
        updated_fields=updated_fields
    )
