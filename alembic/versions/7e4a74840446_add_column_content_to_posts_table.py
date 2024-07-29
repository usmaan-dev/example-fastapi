"""add column content to posts table

Revision ID: 7e4a74840446
Revises: 606532898c4d
Create Date: 2024-07-25 16:20:02.273313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = '7e4a74840446'
down_revision: Union[str, None] = '606532898c4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('body', sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'body')
