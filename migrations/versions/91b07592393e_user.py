"""user

Revision ID: 91b07592393e
Revises: 
Create Date: 2024-04-20 14:42:01.450256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91b07592393e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=False),
    sa.Column('lastname', sa.String(length=64), nullable=False),
    sa.Column('education_text', sa.String(length=256), nullable=False),
    sa.Column('education_level', sa.Integer(), nullable=False),
    sa.Column('experience_text', sa.String(length=512), nullable=False),
    sa.Column('experience_years', sa.Integer(), nullable=False),
    sa.Column('technologies_text', sa.String(length=512), nullable=False),
    sa.Column('soft_skills_text', sa.String(length=512), nullable=False),
    sa.Column('cv_filename', sa.String(length=64), nullable=False),
    sa.Column('cv_pdf_content', sa.LargeBinary(), nullable=False),
    sa.Column('profile_picture_bytes', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
