"""add address column

Revision ID: 111edc136071
Revises: f8fac5f9f1ee
Create Date: 2026-04-24 09:28:01.449653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '111edc136071'
down_revision: Union[str, Sequence[str], None] = 'f8fac5f9f1ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'seller',
        sa.Column('address', sa.Integer(), nullable=False, server_default='0')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('seller', 'address')
