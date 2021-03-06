# Run with "python server.py"
"""
Models and table creation
"""
import uuid
from peewee import *



# Start your code here, good luck (: ...
db = SqliteDatabase('content.db')
KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'


class BaseModel(Model):
    """Base Model to specifiy in only one place which database to use.
    """
    class Meta:
        """Defining which database to use. Is extended by other models.
        """
        database = db


class User(BaseModel):
    """User model
    username is an email and unique.  Id is also added by default for indexing.
    """
    id = CharField(primary_key=True, default=uuid.uuid4)
    username = CharField(unique=True)
    password = CharField()
    token = CharField(null=True)


class Notes(BaseModel):
    """Notes Model
    user is foreign key to User model, Id added by default
    """
    user = ForeignKeyField(User, backref='notes')
    title = CharField()
    content = TextField()


def create_tables():
    """creates tables if not created
    """
    with db:
        db.create_tables([User, Notes])