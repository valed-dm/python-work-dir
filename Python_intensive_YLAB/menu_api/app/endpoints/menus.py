from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


from app import deps
from app.crud.crud_menus import menus
from app.schemas.menus import MenusCreate, MenusUpdate


# APIRouter creates path operations for menus module
router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menus"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=200)
def read_all_menus_items(
    db: Session = Depends(deps.get_db),
):
    """
    READ all menus items
    """
    return menus.get_multi(
        db=db,
        limit=100
    )


@router.get("/{menus_id}", status_code=200)
def read_menus_item(
    menus_id: int,
    db: Session = Depends(deps.get_db),
):
    """
    READ a single menu item
    """
    result = menus.get(db=db, id=menus_id)

    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404,
            # detail=f"Menu item with ID {menu_id} not found"
            detail="menu not found"
        )

    result = jsonable_encoder(result)
    result['id'] = str(result['id'])

    return result


@router.post("", status_code=201)
def create_menus_item(
    menus_item_in: MenusCreate,
    db: Session = Depends(deps.get_db)
):
    """
    CREATE a new menu item.
    """
    menus_item_in = jsonable_encoder(menus_item_in)
    menus_item_in.update({'submenus_counter': 0, 'dishes_counter': 0})

    result = menus.create(db=db, obj_in=menus_item_in)
    result = jsonable_encoder(result)

    result['id'] = str(result['id'])
    result['submenus_counter'] = str(result['submenus_counter'])
    result['dishes_counter'] = str(result['dishes_counter'])

    return result


@router.delete("/{menus_id}", status_code=200)
def delete_menus_item(
    menus_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    DELETE a menu item.
    """
    return menus.remove(
        db=db,
        id=menus_id
    )


@router.patch("/{menus_id}", status_code=200)
def update_menus_item(
    menus_id,
    updated_fields: MenusUpdate,
    db: Session = Depends(deps.get_db)
):
    """
    UPDATE a menu item.
    """
    result = menus.update_item(
        db=db,
        item_id=menus_id,
        updated_fields=updated_fields
    )
    result = jsonable_encoder(result)

    return result
