"""create posts table

Revision ID: 606532898c4d
Revises: 
Create Date: 2024-07-25 16:15:04.748028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa # type: ignore


# revision identifiers, used by Alembic.
revision: str = '606532898c4d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table('posts',
        sa.Column('id', sa.Integer(), primary_key = True, nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('posts')
