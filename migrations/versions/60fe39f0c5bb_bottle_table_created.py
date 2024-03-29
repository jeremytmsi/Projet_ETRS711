"""Bottle table created

Revision ID: 60fe39f0c5bb
Revises: 8929461c3d82
Create Date: 2023-12-12 15:25:42.028172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60fe39f0c5bb'
down_revision: Union[str, None] = '8929461c3d82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bottles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('domain', sa.String(), nullable=True),
    sa.Column('wine_type', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('price', sa.Double(), nullable=True),
    sa.Column('photo_link', sa.String(), nullable=True),
    sa.Column('shelf_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shelf_id'], ['shelfs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bottles_id'), 'bottles', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bottles_id'), table_name='bottles')
    op.drop_table('bottles')
    # ### end Alembic commands ###
