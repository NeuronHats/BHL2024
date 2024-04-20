"""company check

Revision ID: 9964b9cd62d8
Revises: 80d142d90ca5
Create Date: 2024-04-20 16:17:03.610240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9964b9cd62d8'
down_revision = '80d142d90ca5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_company', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_company')

    # ### end Alembic commands ###
