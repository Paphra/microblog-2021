"""add language field to post not to User

Revision ID: c411c6fb9d20
Revises: c3cd62d67aaa
Create Date: 2021-07-23 12:49:40.860792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c411c6fb9d20'
down_revision = 'eaa0816a7e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    op.drop_column('user', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
