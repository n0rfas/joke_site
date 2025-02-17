"""seed_jokes_data

Revision ID: 5a67f860fb79
Revises: 78eb2b86ef83
Create Date: 2025-02-15 15:20:41.330936

"""

from pathlib import Path
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5a67f860fb79"
down_revision: Union[str, None] = "78eb2b86ef83"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def load_jokes() -> list[str]:
    jokes_file = Path(__file__).parent.parent / "data" / "jokes.txt"
    with open(jokes_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def upgrade() -> None:
    jokes = load_jokes()
    conn = op.get_bind()

    for joke in jokes:
        conn.execute(sa.text("INSERT INTO jokes (text) VALUES (:joke)"), {"joke": joke})


def downgrade() -> None:
    jokes = load_jokes()
    conn = op.get_bind()

    conn.execute(
        sa.text("DELETE FROM jokes WHERE text = ANY(:jokes)"), {"jokes": jokes}
    )
