"""add cache

Revision ID: e3aa9796621a
Revises: d25d0d9d25ef
Create Date: 2024-04-21 06:56:57.774952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3aa9796621a'
down_revision = 'd25d0d9d25ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_posting', schema=None) as batch_op:
        batch_op.alter_column('keywords',
               existing_type=sa.String(length=1024),
               type_=sa.TEXT(length=1024),
               nullable=True)

    op.create_table('_alembic_tmp_job_posting',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), nullable=False),
    sa.Column('description', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('location', sa.VARCHAR(length=256), nullable=False),
    sa.Column('salary_range_lower', sa.INTEGER(), nullable=False),
    sa.Column('salary_range_upper', sa.INTEGER(), nullable=False),
    sa.Column('company_id', sa.INTEGER(), nullable=False),
    sa.Column('distance', sa.VARCHAR(length=64), nullable=False),
    sa.Column('keywords', sa.VARCHAR(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###