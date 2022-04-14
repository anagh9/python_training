# Simple Example
from FlaskSqlalchemy import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

"""
Integer - an integer
String(size) - a string with a maximum length (optional in some databases, e.g. PostgreSQL)
Text - some longer unicode text
DateTime - date and time expressed as Python datetime object.
Float - stores floating point values
Boolean - stores a boolean value
PickleType - stores a pickled Python object
LargeBinary - stores large arbitrary binary data
"""

# One-to-Many Relationships
# Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class:

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

# One-to-One Relationships
# One-to-one relationships are expressed with the one_to_one() function:


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True, uselist=False)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

"""
backref is a simple way to also declare a new property on the Address class. You can then also use my_address.person to get to the person at that address. lazy defines when SQLAlchemy will load the data from the database:



    'select' / True (which is the default, but explicit is better than implicit) means that SQLAlchemy will load the data as necessary in one go using a standard select statement.
        
        ex- 
        addresses = db.relationship('Address', lazy='select', backref=db.backref('person', lazy='joined'))


    'joined' / False tells SQLAlchemy to load the relationship in the same query as the parent using a JOIN statement.

    'subquery' works like 'joined' but instead SQLAlchemy will use a subquery.

    'dynamic' is special and can be useful if you have many items and always want to apply additional SQL filters to them. Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading the items. Note that this cannot be turned into a different loading strategy when querying so it’s often a good idea to avoid using this in favor of lazy=True. A query object equivalent to a dynamic user.addresses relationship can be created using Address.query.with_parent(user) while still being able to use lazy or eager loading on the relationship itself as necessary.

"""

# Many to Many Relationships

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# Mixin
from datetime import datetime

class TimestampMixin(object):
    created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)