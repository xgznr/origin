import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql://postgres:qwerty123@localhost:5432/postgres"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String)
    subject_id = Column(Integer)


@pytest.fixture
def db():
    session = SessionLocal()
    session.rollback()
    # Очищаем таблицу ПЕРЕД тестом, чтобы ID всегда был свободен
    session.query(User).delete()
    session.commit()
    yield session
    session.close()


def test_add_user(db):
    new_user = User(user_id=1, user_email="test@mail.com", subject_id=101)
    db.add(new_user)
    db.commit()

    user = db.query(User).filter_by(user_id=1).first()
    assert user is not None
    assert user.user_email == "test@mail.com"


def test_update_user(db):
    user = User(user_id=2, user_email="update@mail.com", subject_id=1)
    db.add(user)
    db.commit()

    user.subject_id = 99
    db.commit()

    updated = db.query(User).filter_by(user_id=2).first()
    assert updated.subject_id == 99


def test_delete_user(db):
    user = User(user_id=3, user_email="delete@mail.com", subject_id=5)
    db.add(user)
    db.commit()

    db.delete(user)
    db.commit()

    deleted = db.query(User).filter_by(user_id=3).first()
    assert deleted is None
