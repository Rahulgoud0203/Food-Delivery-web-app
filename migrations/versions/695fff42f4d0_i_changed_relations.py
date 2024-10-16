"""i changed relations

Revision ID: 695fff42f4d0
Revises: 
Create Date: 2024-10-12 18:46:01.793484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '695fff42f4d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('date_of_joined', sa.DateTime(), nullable=True),
    sa.Column('phone_no', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password_hash')
    )
    op.create_table('restaurents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=30), nullable=False),
    sa.Column('img', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img')
    )
    op.create_table('menu_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('descr', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('img', sa.String(length=64), nullable=True),
    sa.Column('rest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rest_id'], ['restaurents.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descr'),
    sa.UniqueConstraint('img')
    )
    op.create_table('cartitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['menu_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cartitems')
    op.drop_table('menu_items')
    op.drop_table('restaurents')
    op.drop_table('profile')
    # ### end Alembic commands ###
