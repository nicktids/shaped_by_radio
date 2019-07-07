
# not really started this yet
# example
credentials = {
    'username': 'scott',
    'password': 'tiger',
    'host': 'myhost',
    'database': 'databasename',
    'port': '1560'}

import urllib



DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


sess = db.create_scoped_session(options=dict(bind=db.get_engine(app, test_db),binds={}))