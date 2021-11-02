"""empty message

Revision ID: 605394d40899
Revises: 
Create Date: 2021-10-29 11:48:34.942325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605394d40899'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uptime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('started', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uptime')
    # ### end Alembic commands ###