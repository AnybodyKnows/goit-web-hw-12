"""Init

Revision ID: a1799e7a83f6
Revises: e825ae7354f5
Create Date: 2024-07-04 21:53:26.812629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1799e7a83f6'
down_revision: Union[str, None] = 'e825ae7354f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE contacts ALTER COLUMN birthday TYPE DATE USING birthday::date")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=sa.Date(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    # ### end Alembic commands ###