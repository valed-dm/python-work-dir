from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List


from app import deps
from app.crud import crude_dishes as crud
from app.schemas.dishes import Dishes, DishesCreate, DishesUpdate


# APIRouter creates path operations for submenus module
router = APIRouter(
    prefix="/api/v1/menus/{api_test_menus_id}/submenus/{api_test_submenus_id}/dishes",
    tags=["Dishes"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=200)
def read_all_submenus_dishes_items(
    api_test_submenus_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Dishes]:
    """
    READ all submenu dish items
    """
    submenus_dishes_items_list = jsonable_encoder(
        crud.dishes.get_multi(db=db, limit=100))
    return list(filter(
        lambda x: x['menus_id'] == api_test_submenus_id,
        submenus_dishes_items_list
    ))


@router.get("/{api_test_dish_id}", status_code=200)
def read_dish_item(
    api_test_dish_id: int,
    db: Session = Depends(deps.get_db),
):
    """
    READ a single dish item
    """
    result = crud.dishes.get(db=db, id=api_test_dish_id)

    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404,
            # detail=f"Dish item with ID {api_test_dish_id} not found"
            detail="dish not found"
        )

    # result = jsonable_encoder(result)
    # result['id'] = str(result['id'])

    return result


@router.post("", status_code=201)
def create_dish_item(
    api_test_submenus_id: int,
    dish_item_in: DishesCreate,
    db: Session = Depends(deps.get_db)
):
    """
    CREATE a new dish item.
    """
    item_in: dict = jsonable_encoder(dish_item_in)
    item_in.update({'submenus_id': api_test_submenus_id})

    result = crud.dishes.create(db=db, obj_in=item_in)
    result = jsonable_encoder(result)
    result['id'] = str(result['id'])
    result['price'] = str(result['price'])

    return result


@router.delete("/{api_test_dish_id}", status_code=200)
def delete_dish_item(
    api_test_dish_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    DELETE a dish item.
    """
    return crud.dishes.remove(db=db, id=api_test_dish_id)


@router.patch("/{api_test_dish_id}}", status_code=200)
def update_dish_item(
    api_test_dish_id: int,
    updated_fields: DishesUpdate,
    db: Session = Depends(deps.get_db)
):
    """
    UPDATE a dish item.
    """
    return crud.dishes.update_item(
        db=db,
        item_id=api_test_dish_id,
        updated_fields=updated_fields
    )
