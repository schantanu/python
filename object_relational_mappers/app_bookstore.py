from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

book_reader = db.Table('book_reader',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('reader_id', db.Integer, db.ForeignKey('reader.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    books = db.relationship('Book', secondary=book_author, backref='authors', lazy='select')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    books = db.relationship('Book',backref='publisher')

class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    books = db.relationship('Book', secondary=book_reader, backref='readers', lazy='select')

@app.cli.command("initdb")
def reset_db():
    """Drops and Creates fresh database"""
    db.drop_all()
    db.create_all()

    print("Initialized default DB.")

@app.cli.command("bootstrap")
def bootstrap_data():
    """Populates database with data"""

    p1 = Publisher(name='Penguin Random House')
    p2 = Publisher(name='Harper Collins')
    b1 = Book(name='Intro to Python', publisher=p1)
    b2 = Book(name='Intro to C++', publisher=p2)
    b3 = Book(name='Intro to Java', publisher=p2)
    a1 = Author(name='John Carson')
    a2 = Author(name='Eric Jameson')
    r1 = Reader(name='Lily')
    r2 = Reader(name='Sam')

    db.session.add_all([p1,p2,b1,b2,b3,a1,a2,r1,r2])
    b1.authors.extend([a1,a2])
    b2.authors.extend([a1,a2])
    b1.readers.extend([r1,r2])
    b2.readers.extend([r1])

    db.session.commit()

    print("Added data to DB.")

@app.cli.command("query")
def query_data():

    author = Author.query.filter(Author.name.like('John%')).first()

    for book in author.books:
        for reader in book.readers:
            print(f"'{author.name}' has written '{book.name}' published by '{book.publisher.name}', read by '{reader.name}'.")

if __name__ == "__main__":
    app.run()