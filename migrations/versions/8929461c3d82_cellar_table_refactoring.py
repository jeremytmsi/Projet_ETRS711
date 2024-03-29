"""Cellar table refactoring

Revision ID: 8929461c3d82
Revises: 9599b791a90f
Create Date: 2023-12-12 15:18:39.622411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8929461c3d82'
down_revision: Union[str, None] = '9599b791a90f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cellars', 'region')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cellars', sa.Column('region', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
