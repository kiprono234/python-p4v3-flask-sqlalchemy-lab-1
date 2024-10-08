"""initial migration

Revision ID: 0d71fb414980
Revises: 20b9a674f931
Create Date: 2024-10-06 14:06:49.935656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d71fb414980'
down_revision = '20b9a674f931'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('earthquakes', schema=None) as batch_op:
        batch_op.alter_column('magnitude',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('earthquakes', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('magnitude',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###
