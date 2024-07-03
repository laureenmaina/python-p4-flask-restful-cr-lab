"""add columns to table

Revision ID: 82f98cb924ce
Revises: 67f5d67aea55
Create Date: 2024-07-03 12:16:39.160800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82f98cb924ce'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
