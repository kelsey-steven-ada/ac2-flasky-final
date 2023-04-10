"""Added a Caretaker model and established one to many relationship with Cat

Revision ID: 375fb38c48ca
Revises: f8963a0e6fe5
Create Date: 2023-01-05 10:05:35.113413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375fb38c48ca'
down_revision = 'f8963a0e6fe5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('cat', sa.Column('caretaker_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cat', 'caretaker', ['caretaker_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cat', type_='foreignkey')
    op.drop_column('cat', 'caretaker_id')
    op.drop_table('caretaker')
    # ### end Alembic commands ###