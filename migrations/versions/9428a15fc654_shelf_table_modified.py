"""shelf table modified

Revision ID: 9428a15fc654
Revises: f61cfd53c08f
Create Date: 2024-01-07 10:42:28.011235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9428a15fc654'
down_revision: Union[str, None] = 'f61cfd53c08f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shelfs', sa.Column('region', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shelfs', 'region')
    # ### end Alembic commands ###
