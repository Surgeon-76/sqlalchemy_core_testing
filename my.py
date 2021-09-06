#from fastapi import FastAPI
from sqlalchemy import *

import databases


user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'alchemy_core_db'

#database = databases.Database(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")
#metadata = sqlalchemy.MetaData()
engine = create_engine(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")
engine.connect()
print(engine)