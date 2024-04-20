"""optional fileds in user

Revision ID: 0321843f6afc
Revises: 91b07592393e
Create Date: 2024-04-20 14:51:18.876831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0321843f6afc'
down_revision = '91b07592393e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('firstname',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('lastname',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('education_text',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('education_level',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('experience_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
        batch_op.alter_column('experience_years',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('technologies_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
        batch_op.alter_column('soft_skills_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
        batch_op.alter_column('cv_filename',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('cv_pdf_content',
               existing_type=sa.BLOB(),
               nullable=True)
        batch_op.alter_column('profile_picture_bytes',
               existing_type=sa.BLOB(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('profile_picture_bytes',
               existing_type=sa.BLOB(),
               nullable=False)
        batch_op.alter_column('cv_pdf_content',
               existing_type=sa.BLOB(),
               nullable=False)
        batch_op.alter_column('cv_filename',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('soft_skills_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
        batch_op.alter_column('technologies_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
        batch_op.alter_column('experience_years',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('experience_text',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
        batch_op.alter_column('education_level',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('education_text',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('lastname',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('firstname',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###