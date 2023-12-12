"""create Shelf table

Revision ID: 9599b791a90f
Revises: 645b1d2bf729
Create Date: 2023-12-12 15:17:02.173849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9599b791a90f'
down_revision: Union[str, None] = '645b1d2bf729'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shelfs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('available_bottles', sa.Integer(), nullable=True),
    sa.Column('cellar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cellar_id'], ['cellars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shelfs_id'), 'shelfs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shelfs_id'), table_name='shelfs')
    op.drop_table('shelfs')
    # ### end Alembic commands ###