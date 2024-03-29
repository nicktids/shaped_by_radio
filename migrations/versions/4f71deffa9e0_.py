"""empty message

Revision ID: 4f71deffa9e0
Revises: b8d85678a28b
Create Date: 2019-09-13 20:30:34.943648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f71deffa9e0'
down_revision = 'b8d85678a28b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(length=100), nullable=True),
    sa.Column('musicbrainz_gid', sa.String(length=100), nullable=True),
    sa.Column('bbc_artist_pid', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('broadcast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.String(length=10), nullable=True),
    sa.Column('shortname', sa.String(length=10), nullable=True),
    sa.Column('presenter', sa.String(length=100), nullable=True),
    sa.Column('show_name', sa.String(length=100), nullable=True),
    sa.Column('first_broadcast_date', sa.Date(), nullable=True),
    sa.Column('image_pid', sa.String(length=20), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('track_title', sa.String(length=200), nullable=True),
    sa.Column('bbc_track_pid', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('ep_pid', sa.String(length=20), nullable=True),
    sa.Column('image_pid', sa.String(length=20), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc_short', sa.String(length=200), nullable=True),
    sa.Column('desc_med', sa.String(length=500), nullable=True),
    sa.Column('desc_long', sa.String(length=3000), nullable=True),
    sa.Column('broadcast_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['broadcast_id'], ['broadcast.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show_track_position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.Column('show_position', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Float(), nullable=True),
    sa.Column('show_offset', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['track.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('special_title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.Column('special_title', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['track.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('episode')
    op.drop_table('broadcaster')
    op.drop_table('films')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('director', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('year', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('broadcaster',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('broadcast_pid', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('show_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('station_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], name='broadcaster_station_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='broadcaster_pkey')
    )
    op.create_table('episode',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='episode_pkey')
    )
    op.drop_table('special_title')
    op.drop_table('show_track_position')
    op.drop_table('show')
    op.drop_table('track')
    op.drop_table('broadcast')
    op.drop_table('artist')
    # ### end Alembic commands ###
