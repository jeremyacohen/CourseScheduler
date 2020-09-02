"""empty message

Revision ID: dfc5c35db454
Revises: 350cb8049510
Create Date: 2020-03-29 03:25:44.299649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc5c35db454'
down_revision = '350cb8049510'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('departmentdos',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('professortres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('unit', sa.Float(precision=2, asdecimal=1), nullable=False),
    sa.Column('alp', sa.Boolean(), nullable=False),
    sa.Column('cz', sa.Boolean(), nullable=False),
    sa.Column('ns', sa.Boolean(), nullable=False),
    sa.Column('qs', sa.Boolean(), nullable=False),
    sa.Column('ss', sa.Boolean(), nullable=False),
    sa.Column('cci', sa.Boolean(), nullable=False),
    sa.Column('ei', sa.Boolean(), nullable=False),
    sa.Column('sts', sa.Boolean(), nullable=False),
    sa.Column('fl', sa.Boolean(), nullable=False),
    sa.Column('r', sa.Boolean(), nullable=False),
    sa.Column('w', sa.Boolean(), nullable=False),
    sa.Column('rating', sa.Float(precision=2, asdecimal=1), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['subject'], ['departmentdos.name'], ),
    sa.PrimaryKeyConstraint('subject', 'num')
    )
    op.create_table('corequisitedos',
    sa.Column('main_subject', sa.String(length=32), nullable=False),
    sa.Column('main_num', sa.Integer(), nullable=False),
    sa.Column('main_type', sa.String(length=32), nullable=False),
    sa.Column('sup_subject', sa.String(length=32), nullable=False),
    sa.Column('sup_num', sa.Integer(), nullable=False),
    sa.Column('sup_type', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['main_subject', 'main_num'], ['classdos.subject', 'classdos.num'], ),
    sa.ForeignKeyConstraint(['sup_subject', 'sup_num'], ['classdos.subject', 'classdos.num'], ),
    sa.PrimaryKeyConstraint('sup_subject', 'sup_num', 'sup_type')
    )
    op.create_table('courseoffdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('course_num', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mon', sa.Boolean(), nullable=False),
    sa.Column('tues', sa.Boolean(), nullable=False),
    sa.Column('wed', sa.Boolean(), nullable=False),
    sa.Column('thur', sa.Boolean(), nullable=False),
    sa.Column('fri', sa.Boolean(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['subject', 'course_num'], ['classdos.subject', 'classdos.num'], ),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id')
    )
    op.create_table('courseprofdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('course_num', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prof_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(precision=2, asdecimal=1), nullable=True),
    sa.ForeignKeyConstraint(['prof_id'], ['professortres.id'], ),
    sa.ForeignKeyConstraint(['subject', 'course_num', 'type', 'id'], ['courseoffdos.subject', 'courseoffdos.course_num', 'courseoffdos.type', 'courseoffdos.id'], ),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id', 'prof_id')
    )
    op.drop_table('professordos')
    op.create_foreign_key(None, 'class', 'department', ['subject'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'class', type_='foreignkey')
    op.create_table('professordos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='professordos_pkey')
    )
    op.drop_table('courseprofdos')
    op.drop_table('courseoffdos')
    op.drop_table('corequisitedos')
    op.drop_table('classdos')
    op.drop_table('professortres')
    op.drop_table('departmentdos')
    op.drop_table('department')
    # ### end Alembic commands ###