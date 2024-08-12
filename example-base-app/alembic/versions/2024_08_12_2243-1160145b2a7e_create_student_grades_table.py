"""create student_grades table

Revision ID: 1160145b2a7e
Revises: 37c9ad82863a
Create Date: 2024-08-12 22:43:49.772361

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1160145b2a7e"
down_revision: Union[str, None] = "37c9ad82863a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "student_grades",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("subject", sa.String(length=40), nullable=False),
        sa.Column("grade", sa.Integer(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["students.id"],
            name=op.f("fk_student_grades_student_id_students"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_student_grades")),
    )


def downgrade() -> None:
    op.drop_table("student_grades")
