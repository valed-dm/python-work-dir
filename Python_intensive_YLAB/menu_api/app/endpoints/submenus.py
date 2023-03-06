from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import update
from sqlalchemy.orm import Session
from typing import List


from app import deps
from app.crud.crud_menus import menus
from app.crud.crude_submenus import submenus
from app.schemas.submenus import Submenus, SubmenusCreate, SubmenusUpdate


# APIRouter creates path operations for submenus module
router = APIRouter(
    prefix="/api/v1/menus/{api_test_menus_id}/submenus",
    tags=["Submenus"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=200)
def read_all_submenus_items(
    api_test_menus_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Submenus]:
    """
    READ all submenus items
    """
    submenus_items_list = jsonable_encoder(
        submenus.get_multi(db=db, limit=100))
    return list(filter(
        lambda x: x['menus_id'] == api_test_menus_id,
        submenus_items_list
    ))


@router.get("/{api_test_submenus_id}", status_code=200)
def read_submenus_item(
    api_test_submenus_id: int,
    db: Session = Depends(deps.get_db),
):
    """
    READ a single submenus item
    """
    result = submenus.get(db=db, id=api_test_submenus_id)

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
def create_submenus_item(
    api_test_menus_id: int,
    submenus_item_in: SubmenusCreate,
    db: Session = Depends(deps.get_db)
):
    """
    CREATE a new submenus item.
    """
    # create submenus
    item_in: dict = jsonable_encoder(submenus_item_in)
    item_in.update({'menus_id': api_test_menus_id, 'dishes_counter': 0})

    result = submenus.create(db=db, obj_in=item_in)
    result = jsonable_encoder(result)

    result['id'] = str(result['id'])
    result['menus_id'] = str(result['menus_id'])
    result['dishes_counter'] = str(result['dishes_counter'])
    print(result)

    # update submenus_counter in menus table
    menus_in = menus.get(db=db, id=api_test_menus_id)
    menus_in: dict = jsonable_encoder(menus_in)
    print(menus_in)
    new_submenus_counter = menus_in['submenus_counter'] + 1
    updated_fields = {'submenus_counter': new_submenus_counter}
    print(updated_fields)
    menus.update_item(
        db=db,
        item_id=api_test_menus_id,
        updated_fields=updated_fields
    )

    return result


@router.delete("/{api_test_submenus_id}", status_code=200)
def delete_submenus_item(
    api_test_submenus_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    DELETE a submenus item.
    """
    # get menus_id
    submenus_item = submenus.get(db=db, id=api_test_submenus_id)
    submenus_item = jsonable_encoder(submenus_item)
    menus_id = submenus_item['menus_id']

    # update submenus_counter
    menus_to_update = menus.get(db=db, id=menus_id)
    menus_to_update = jsonable_encoder(menus_to_update)
    new_submenus_counter = menus_to_update['submenus_counter'] - 1
    menus_to_update.update({'submenus_counter': new_submenus_counter})
    menus.update_item(
        db=db,
        item_id=menus_id,
        updated_fields=menus_to_update
    )

    # delete submenus
    return submenus.remove(db=db, id=api_test_submenus_id)


@router.patch("/{api_test_submenus_id}", status_code=200)
def update_submenus_item(
    api_test_submenus_id: int,
    updated_fields: SubmenusUpdate,
    db: Session = Depends(deps.get_db)
):
    """
    UPDATE a submenus item.
    """
    result = submenus.update_item(
        db=db,
        item_id=api_test_submenus_id,
        updated_fields=updated_fields
    )
    result = jsonable_encoder(result)

    return result
