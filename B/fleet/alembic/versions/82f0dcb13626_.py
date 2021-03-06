"""empty message

Revision ID: 82f0dcb13626
Revises: 
Create Date: 2022-02-04 18:05:47.171215

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '82f0dcb13626'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('first_lastname', sa.String(length=120), nullable=True),
    sa.Column('second_lastname', sa.String(length=120), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('credential_type', sa.String(length=5), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=True),
    sa.Column('brand', sa.String(length=120), nullable=True),
    sa.Column('vehicle_type', sa.String(length=120), nullable=True),
    sa.Column('maximum_laded_weight', sa.Float(), nullable=False),
    sa.Column('VIN', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('VIN')
    )
    op.create_table('assignments',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('vehicle_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('driver_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('expiration_date', sa.DateTime(), nullable=False),
    sa.Column('is_expired', sa.Boolean(), nullable=True),
    sa.Column('area', sa.String(length=300), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments')
    op.drop_table('vehicles')
    op.drop_table('drivers')
    # ### end Alembic commands ###
