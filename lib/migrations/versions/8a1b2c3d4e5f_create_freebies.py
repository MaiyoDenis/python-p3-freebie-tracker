"""create freebies table

Revision ID: 8a1b2c3d4e5f
Revises: 5f72c58bf48c
Create Date: 2024-06-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a1b2c3d4e5f'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('freebies')
