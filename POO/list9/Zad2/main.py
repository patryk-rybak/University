from models import Base, Parent, Child
from db import engine
from session import Session

def init_db():
    Base.metadata.create_all(engine)

def add_sample_data():
    session = Session()

    parent = Parent(name="Anna")
    parent.children = [
        Child(name="Zosia"),
        Child(name="Tomek")
    ]
    session.add(parent)
    session.commit()
    session.close()

def read_data():
    session = Session()
    parents = session.query(Parent).all()
    print()
    print()
    print()
    breakpoint()
    for p in parents:
        print(f"{p.name}: {[c.name for c in p.children]}")
    session.close()

if __name__ == "__main__":
    init_db()
    add_sample_data()
    read_data()

