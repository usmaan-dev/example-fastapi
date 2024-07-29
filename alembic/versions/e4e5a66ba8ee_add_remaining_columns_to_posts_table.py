"""add remaining columns to posts table

Revision ID: e4e5a66ba8ee
Revises: 42e456273ab1
Create Date: 2024-07-25 17:08:18.621566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = 'e4e5a66ba8ee'
down_revision: Union[str, None] = '42e456273ab1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('now()')))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
