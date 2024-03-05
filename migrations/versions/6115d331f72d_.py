"""empty message

Revision ID: 6115d331f72d
Revises: 0b1f1848e7e8
Create Date: 2024-03-04 22:51:07.940291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6115d331f72d'
down_revision = '0b1f1848e7e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('tour_id', sa.Integer(), nullable=False),
    sa.Column('people', sa.Integer(), nullable=True),
    sa.Column('datecreated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['tour.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    # ### end Alembic commands ###
