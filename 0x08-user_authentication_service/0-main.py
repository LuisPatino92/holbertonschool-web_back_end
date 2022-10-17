#!/usr/bin/env python3
""" Module docstring """

from user import User

print(User.__tablename__)

for field in User.__table__.columns:
    print(f"{field: {field.type}")
