"""empty message

Revision ID: e685e77e6ad7
Revises: 98df3a287f02
Create Date: 2019-12-15 16:21:46.457306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e685e77e6ad7'
down_revision = '98df3a287f02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=1200),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=1200),
               nullable=False)
    # ### end Alembic commands ###
