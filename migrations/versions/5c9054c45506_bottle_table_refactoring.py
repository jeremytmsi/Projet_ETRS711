"""bottle table refactoring

Revision ID: 5c9054c45506
Revises: 60fe39f0c5bb
Create Date: 2023-12-12 15:34:24.789223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c9054c45506'
down_revision: Union[str, None] = '60fe39f0c5bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bottles', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bottles', 'quantity')
    # ### end Alembic commands ###
