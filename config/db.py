from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

base_dir=Path(__file__).parent.parent

SQLAlchemy_db=f'sqlite:///{base_dir}/user.db'

connect_args={'check_same_thread':False}
engine=create_engine(SQLAlchemy_db,connect_args=connect_args)

Session=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


