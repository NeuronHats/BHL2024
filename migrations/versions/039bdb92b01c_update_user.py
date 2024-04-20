"""update user

Revision ID: 039bdb92b01c
Revises: 7078ab1fe2ad
Create Date: 2024-04-20 22:44:02.751288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '039bdb92b01c'
down_revision = '7078ab1fe2ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_company')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'company', ['company_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('company_id')

    op.create_table('_alembic_tmp_company',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('address', sa.VARCHAR(length=256), nullable=False),
    sa.Column('description', sa.VARCHAR(length=512), nullable=False),
    sa.Column('company_size_lower', sa.INTEGER(), nullable=False),
    sa.Column('company_size_higher', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
