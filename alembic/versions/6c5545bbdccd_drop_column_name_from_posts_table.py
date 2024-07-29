"""drop column name from posts table

Revision ID: 6c5545bbdccd
Revises: 7e4a74840446
Create Date: 2024-07-25 16:25:16.976032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = '6c5545bbdccd'
down_revision: Union[str, None] = '7e4a74840446'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('posts', 'name')


def downgrade() -> None:
    op.add_column('posts', sa.Column('name', sa.Integer, nullable=True))
