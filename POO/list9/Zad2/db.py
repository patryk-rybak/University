from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://orm_user:orm_password@localhost:5432/orm_demo"


engine = create_engine(DATABASE_URL, echo=True)

