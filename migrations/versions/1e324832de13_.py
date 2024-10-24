"""empty message

Revision ID: 1e324832de13
Revises: 
Create Date: 2024-10-23 12:20:03.884245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e324832de13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('retos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_reto', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('clasificaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('posicion', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('puntos', sa.Integer(), nullable=True),
    sa.Column('retos_completados', sa.Integer(), nullable=True),
    sa.Column('reto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reto_id'], ['retos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clasificaciones')
    op.drop_table('usuarios')
    op.drop_table('retos')
    # ### end Alembic commands ###
