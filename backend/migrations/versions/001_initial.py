"""Initial schema: 7 tables per ERD.

Revision ID: 001_initial
Revises: 
Create Date: 2026-10-22 08:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create 7 tables for Otomotif AI ERD."""
    # 1. vehicles table
    op.create_table(
        'vehicles',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('brand', sa.String(50), nullable=False),
        sa.Column('model', sa.String(100), nullable=False),
        sa.Column('year_start', sa.Integer(), nullable=False),
        sa.Column('year_end', sa.Integer(), nullable=True),
        sa.Column('category', sa.String(30), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # 2. symptoms table
    op.create_table(
        'symptoms',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('symptom_code', sa.String(20), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('category', sa.String(50), nullable=True),
        sa.Column('embedding', sa.NUMERIC(precision=1536), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('symptom_code', name='uq_symptom_code')
    )

    # 3. diagnoses table
    op.create_table(
        'diagnoses',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('title', sa.String(150), nullable=False),
        sa.Column('technical_explanation', sa.Text(), nullable=False),
        sa.Column('severity_level', sa.Enum('DIY_EASY', 'DIY_HARD', 'WORKSHOP_REQUIRED', name='severity_level'), nullable=False),
        sa.Column('repair_steps', postgresql.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # 4. spare_parts table
    op.create_table(
        'spare_parts',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('part_name', sa.String(150), nullable=False),
        sa.Column('part_number', sa.String(50), nullable=False),
        sa.Column('brand', sa.String(50), nullable=True),
        sa.Column('price_min', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('price_max', sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column('shopee_item_id', sa.String(50), nullable=True),
        sa.Column('shopee_shop_id', sa.String(50), nullable=True),
        sa.Column('default_shopee_url', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # 5. workshops table
    op.create_table(
        'workshops',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('address', sa.Text(), nullable=False),
        sa.Column('latitude', sa.Float(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=False),
        sa.Column('phone', sa.String(20), nullable=True),
        sa.Column('specialties', postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column('rating', sa.Float(), nullable=True),
        sa.Column('review_count', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # 6. symptom_diagnosis_map table (many-to-many)
    op.create_table(
        'symptom_diagnosis_map',
        sa.Column('symptom_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('diagnosis_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('confidence_weight', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['diagnosis_id'], ['diagnoses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('symptom_id', 'diagnosis_id'),
        sa.UniqueConstraint('symptom_id', 'diagnosis_id', name='uq_symptom_diagnosis_map')
    )

    # 7. diagnosis_part_map table (many-to-many)
    op.create_table(
        'diagnosis_part_map',
        sa.Column('diagnosis_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('spare_part_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('is_primary', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['diagnosis_id'], ['diagnoses.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['spare_part_id'], ['spare_parts.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('diagnosis_id', 'spare_part_id'),
        sa.UniqueConstraint('diagnosis_id', 'spare_part_id', name='uq_diagnosis_part')
    )

    # Association tables
    op.create_table(
        'vehicle_symptom',
        sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('symptom_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('vehicle_id', 'symptom_id')
    )

    op.create_table(
        'vehicle_workshop',
        sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('workshop_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['workshop_id'], ['workshops.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('vehicle_id', 'workshop_id')
    )


def downgrade() -> None:
    """Drop all tables."""
    op.drop_table('vehicle_workshop')
    op.drop_table('vehicle_symptom')
    op.drop_table('diagnosis_part_map')
    op.drop_table('symptom_diagnosis_map')
    op.drop_table('workshops')
    op.drop_table('spare_parts')
    op.drop_table('diagnoses')
    op.drop_table('symptoms')
    op.drop_table('vehicles')
