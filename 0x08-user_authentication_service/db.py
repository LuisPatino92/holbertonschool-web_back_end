#!/usr/bin/env python3
""" Module docstring """

import sqlalchemy
from typing import TypeVar
from user import (
    Base,
    User,
)

declarative_base = sqlalchemy.ext.declarative.declarative_base
create_engine = sqlalchemy.create_engine
sessionmaker = sqlalchemy.orm.sessionmaker
InvalidRequestError = sqlalchemy.exc.InvalidRequestError
NoResultFound = sqlalchemy.orm.exc.NoResultFound


class DB:
    """ Relational mapper class """

    def __init__(self):
        """ Constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Getter for a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds User """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """ Finds an user"""
        if not kwargs:
            raise InvalidRequestError

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update User """
        user = self.find_user_by(id=user_id)

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
