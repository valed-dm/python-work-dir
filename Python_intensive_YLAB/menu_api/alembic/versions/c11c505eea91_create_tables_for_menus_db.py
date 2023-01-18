"""create tables for menus db

Revision ID: c11c505eea91
Revises: 
Create Date: 2023-01-18 09:20:14.494576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c11c505eea91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_item', sa.String(length=64), nullable=False),
    sa.Column('menu_description', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('menu_item', name='_menu_item_uc')
    )
    op.create_table('submenus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submenu_item', sa.String(length=64), nullable=False),
    sa.Column('submenu_description', sa.String(length=256), nullable=True),
    sa.Column('menus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menus_id'], ['menus.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submenu_item', name='_submenu_item_uc')
    )
    op.create_table('dishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dish_name', sa.String(length=64), nullable=False),
    sa.Column('dish_description', sa.String(length=256), nullable=True),
    sa.Column('dish_price', sa.Numeric(precision=8, scale=2), nullable=False),
    sa.Column('submenus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['submenus_id'], ['submenus.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dish_name', name='_dish_name_uc')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dishes')
    op.drop_table('submenus')
    op.drop_table('menus')
    # ### end Alembic commands ###
