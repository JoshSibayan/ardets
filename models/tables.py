# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

db.define_table('project',
                Field('project_name', 'text'),
                Field('phase', 'text'),
                Field('version', 'text'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow())
                )

db.project.project_name.requires = IS_NOT_EMPTY()
db.project.phase.requires = IS_NOT_EMPTY()
db.project.version.requires = IS_NOT_EMPTY()

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
