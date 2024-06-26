"""fix:


Revision ID: 22568a0b3745
Revises: 9964b9cd62d8
Create Date: 2024-04-20 16:25:21.950180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22568a0b3745'
down_revision = '9964b9cd62d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_user')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_company', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_company')

    op.create_table('_alembic_tmp_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=256), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=64), nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=64), nullable=False),
    sa.Column('education_text', sa.VARCHAR(length=256), nullable=False),
    sa.Column('education_level', sa.INTEGER(), nullable=False),
    sa.Column('experience_text', sa.VARCHAR(length=512), nullable=False),
    sa.Column('experience_years', sa.INTEGER(), nullable=False),
    sa.Column('technologies_text', sa.VARCHAR(length=512), nullable=False),
    sa.Column('soft_skills_text', sa.VARCHAR(length=512), nullable=False),
    sa.Column('cv_filename', sa.VARCHAR(length=64), nullable=False),
    sa.Column('cv_pdf_content', sa.BLOB(), nullable=False),
    sa.Column('profile_picture_bytes', sa.BLOB(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
