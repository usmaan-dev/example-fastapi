"""add foreign key to posts table

Revision ID: 42e456273ab1
Revises: e16f0e062753
Create Date: 2024-07-25 16:55:59.474277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = '42e456273ab1'
down_revision: Union[str, None] = 'e16f0e062753'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fkey', source_table = 'posts', referent_table = 'users',
                          local_cols = ['owner_id'], remote_cols = ['id'], ondelete = 'CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name = 'posts', type_ = 'foreignkey')
    op.drop_column('posts', 'owner_id')
    
