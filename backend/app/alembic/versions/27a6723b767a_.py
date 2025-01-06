"""empty message

Revision ID: 27a6723b767a
Revises: d2ad44deab20
Create Date: 2024-11-29 20:38:05.773083

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "27a6723b767a"
down_revision = "d2ad44deab20"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chat_messages",
        sa.Column("is_best_answer", sa.Boolean(), server_default="0", nullable=False),
    )
    op.create_index(
        "ix_chat_message_is_best_answer",
        "chat_messages",
        ["is_best_answer"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_chat_message_is_best_answer", table_name="chat_messages")
    op.drop_column("chat_messages", "is_best_answer")
    # ### end Alembic commands ###
