"""create quartal_grade table

Revision ID: 5adddd614cde
Revises: 1160145b2a7e
Create Date: 2024-08-12 22:47:52.293751

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5adddd614cde"
down_revision: Union[str, None] = "1160145b2a7e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "quartal_grades",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quartal", sa.String(length=40), nullable=False),
        sa.Column("subject", sa.String(length=40), nullable=False),
        sa.Column("grade", sa.Integer(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["students.id"],
            name=op.f("fk_quartal_grades_student_id_students"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_quartal_grades")),
    )


def downgrade() -> None:
    op.drop_table("quartal_grades")
