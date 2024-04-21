"""add cache

Revision ID: d25d0d9d25ef
Revises: d14bbea1bdb4
Create Date: 2024-04-21 06:53:21.790487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd25d0d9d25ef'
down_revision = 'd14bbea1bdb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('summary', sa.String(length=2048), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('job_posting', schema=None) as batch_op:
        batch_op.alter_column('keywords',
               existing_type=sa.TEXT(length=1024),
               type_=sa.String(length=1024),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_posting', schema=None) as batch_op:
        batch_op.alter_column('keywords',
               existing_type=sa.String(length=1024),
               type_=sa.TEXT(length=1024),
               existing_nullable=True)

    op.drop_table('cache')
    # ### end Alembic commands ###
