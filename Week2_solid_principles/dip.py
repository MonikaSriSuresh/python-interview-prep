"""
Dependency Inversion Principle
"""

from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def save(self):
        pass


class MySQLDatabase(Database):

    def save(self):
        print("Saving To MySQL")


class PostgreSQLDatabase(Database):

    def save(self):
        print("Saving To PostgreSQL")


class UserService:

    def __init__(self, db):
        self.db = db

    def save_user(self):
        self.db.save()


database = MySQLDatabase()

service = UserService(database)

service.save_user()