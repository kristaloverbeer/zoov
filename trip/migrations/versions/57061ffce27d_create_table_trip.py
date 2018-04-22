"""create table trip

Revision ID: 57061ffce27d
Revises: 
Create Date: 2018-04-22 16:00:14.647378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57061ffce27d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('bike_id', sa.String(), nullable=True),
    sa.Column('locations', sa.JSON(), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=True),
    sa.Column('ended_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip')
    # ### end Alembic commands ###
