"""Add users table and workshops.website.

Revision ID: 002_users
Revises: 001_initial
Create Date: 2026-11-16 20:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '002_users'
down_revision = '001_initial'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('full_name', sa.String(150), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email', name='uq_users_email'),
    )
    op.add_column('workshops', sa.Column('website', sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column('workshops', 'website')
    op.drop_table('users')
