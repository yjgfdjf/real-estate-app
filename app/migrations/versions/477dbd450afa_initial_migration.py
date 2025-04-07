"""Initial migration

Revision ID: 477dbd450afa
Revises: be68d0b565f6
Create Date: 2025-03-03 01:39:30.438457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '477dbd450afa'
down_revision: Union[str, None] = 'be68d0b565f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listing_photos',
    sa.Column('photo_id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.listing_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('photo_id')
    )
    op.create_index(op.f('ix_listing_photos_photo_id'), 'listing_photos', ['photo_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_listing_photos_photo_id'), table_name='listing_photos')
    op.drop_table('listing_photos')
    # ### end Alembic commands ###
