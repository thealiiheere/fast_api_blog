"""add_phone_to_users

Revision ID: dc06f7fd4277
Revises: dde570ee44dc
Create Date: 2026-10-07 08:58:16.426714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc06f7fd4277'
down_revision: Union[str, Sequence[str], None] = 'dde570ee44dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
