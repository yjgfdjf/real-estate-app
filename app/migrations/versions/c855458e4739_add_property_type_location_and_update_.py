"""Add property_type, location and update listings

Revision ID: c855458e4739
Revises: 477dbd450afa
Create Date: 2025-03-23 22:53:47.542513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c855458e4739'
down_revision: Union[str, None] = '477dbd450afa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_types',
    sa.Column('property_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('property_type_id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_property_types_property_type_id'), 'property_types', ['property_type_id'], unique=False)
    op.add_column('listings', sa.Column('property_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'listings', 'property_types', ['property_type_id'], ['property_type_id'])
    op.drop_column('listings', 'title')
    op.drop_column('listings', 'property_type')
    op.drop_column('listings', 'location')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listings', sa.Column('location', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('listings', sa.Column('property_type', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('listings', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'listings', type_='foreignkey')
    op.drop_column('listings', 'property_type_id')
    op.drop_index(op.f('ix_property_types_property_type_id'), table_name='property_types')
    op.drop_table('property_types')
    # ### end Alembic commands ###
