"""empty message

Revision ID: 1bae942e7822
Revises: 1434aa1181d2
Create Date: 2020-04-07 18:18:10.359096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bae942e7822'
down_revision = '1434aa1181d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')

    op.alter_column('todos', 'completed', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
