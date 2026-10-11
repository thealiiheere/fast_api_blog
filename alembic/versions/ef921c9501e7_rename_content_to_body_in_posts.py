"""rename_content_to_body_in_posts

Revision ID: ef921c9501e7
Revises: dc06f7fd4277
Create Date: 2026-10-07 09:00:43.905723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef921c9501e7'
down_revision: Union[str, Sequence[str], None] = 'dc06f7fd4277'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
