from db_setup import user_details,engine,Base

Base.metadata.create_all(engine)