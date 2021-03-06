"""empty message

Revision ID: e027e0450d70
Revises: 8a7f64995e70
Create Date: 2020-03-24 23:28:22.319517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e027e0450d70'
down_revision = '8a7f64995e70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courseofftest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courseofftest',
    sa.Column('course_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_type', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('time', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('course_name', 'course_type', 'course_id', name='courseofftest_pkey')
    )
    # ### end Alembic commands ###
