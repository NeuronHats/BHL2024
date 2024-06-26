"""add keyword_match

Revision ID: b75f348c7ec1
Revises: e3aa9796621a
Create Date: 2024-04-21 07:21:04.606241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b75f348c7ec1'
down_revision = 'e3aa9796621a'
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
               existing_nullable=True)

    with op.batch_alter_table('cache', schema=None) as batch_op:
        batch_op.drop_column('keyword_match')

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
