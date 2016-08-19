from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.dialects.postgresql import JSON

meta = MetaData()

users = Table(
				'requests', meta,
				Column('id', Integer, primary_key=True)
				Column('num_requests', Integer, index=True)
)

def upgrade(migrate_engine):
	meta.bind = migrate_engine
	users.create()

def downgrade(migrate_engine):
	meta.bind = migrate_engine
	users.drop()
