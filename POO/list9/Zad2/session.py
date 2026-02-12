from sqlalchemy.orm import sessionmaker, scoped_session
from db import engine

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


# każda funkcja/żądanie dostaje własną sesję