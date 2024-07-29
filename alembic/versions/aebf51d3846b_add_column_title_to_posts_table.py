"""add column title to posts table

Revision ID: aebf51d3846b
Revises: 6c5545bbdccd
Create Date: 2024-07-25 16:31:16.252473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = 'aebf51d3846b'
down_revision: Union[str, None] = '6c5545bbdccd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('title', sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'title')

