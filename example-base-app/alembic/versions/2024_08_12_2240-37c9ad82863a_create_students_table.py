"""create students table

Revision ID: 37c9ad82863a
Revises: 2b51185a4a94
Create Date: 2024-08-12 22:40:10.454006

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "37c9ad82863a"
down_revision: Union[str, None] = "2b51185a4a94"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=40), nullable=False),
        sa.Column("last_name", sa.String(length=40), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_students")),
    )


def downgrade() -> None:
    op.drop_table("students")
