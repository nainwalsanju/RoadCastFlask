from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

 
class InfoModel(db.Model):
    __tablename__ = 'book_table'
    #__bind_key__ = 'db1'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    year = db.Column(db.Integer())
    author=db.Column(db.String())
    price=db.Column(db.Float())

    def __init__(self, name,year,author,price):
        self.name = name
        self.year = year
        self.author = author
        self.price = price
 
    def __repr__(self):
        return f"{self.name}:{self.year}:{self.author}:{self.price}"

class AuthorModel(db.Model):
    __tablename__ = 'author_table'
    __bind_key__ = 'db2'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer())

    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.age}"