"""add_phone_to_users

Revision ID: dde570ee44dc
Revises: 74f815dbdce7
Create Date: 2026-10-05 16:01:53.626556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dde570ee44dc'
down_revision: Union[str, Sequence[str], None] = '74f815dbdce7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
