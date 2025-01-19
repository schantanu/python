from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

user_challenge = db.Table('user_challenge',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

post_challenge = db.Table('post_challenge',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    challenges = db.relationship('Challenge', secondary=user_challenge, backref='users', lazy='select')
    entries = db.relationship('Entry', backref='user')
    posts = db.relationship('Post', backref='user')

    # Attributes
    name = db.Column(db.String(20))

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entries = db.relationship('Entry', backref='challenge')

    # Attributes
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Attributes
    name = db.Column(db.String(20))
    enrolled = db.Column(db.Boolean())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    challenges = db.relationship('Challenge', secondary=post_challenge, backref='posts', lazy='select')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Attributes
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))

@app.cli.command("initdb")
def reset_db():
    """Drops and Creates fresh database"""
    db.drop_all()
    db.create_all()

    print("Initialized default DB.")

@app.cli.command("bootstrap")
def bootstrap_data():
    """Populates database with data"""

    # Users
    u1 = User(name='John Adams')
    u2 = User(name='Eric Smith')

    # Posts
    p1 = Post(name='70 kg',type='Weight',user_id=1)
    p2 = Post(name='69 kg',type='Weight',user_id=1)
    p3 = Post(name='55 kg',type='Weight',user_id=2)
    p4 = Post(name='54 kg',type='Weight',user_id=2)
    p5 = Post(name='30 min',type='Run',user_id=1)
    p6 = Post(name='28 min',type='Run',user_id=1)
    p7 = Post(name='50 min',type='Run',user_id=2)
    p8 = Post(name='49 min',type='Run',user_id=2)

    # Challenges
    c1 = Challenge(name='Weight Loss', type='Weight')
    c2 = Challenge(name='5K Run', type='Run')

    # Entries
    e1 = Entry(name='e1',user_id=1,enrolled=False)
    e2 = Entry(name='e2',user_id=1,enrolled=False)
    e3 = Entry(name='e3',user_id=2,enrolled=True)
    e4 = Entry(name='e4',user_id=1,enrolled=True)
    e5 = Entry(name='e5',user_id=2,enrolled=True)

    # Add
    db.session.add_all([u1,u2,p1,p2,p3,p4,p5,p6,p7,
                        p8,c1,c2,e1,e2,e3,e4,e5])

    c1.entries.extend([e1,e2,e3])
    c2.entries.extend([e4,e5])

    c1.users.extend([u1,u2])
    c2.users.extend([u1,u2])

    db.session.commit()

    print("Added data to DB.")

@app.cli.command("query")
def query_data():

    challenge = Challenge.query.filter_by(type='Run').first()
    posts = Post.query.all()

    for entry in challenge.entries:
        if entry.enrolled is True:
            print(f"The challenge '{challenge.name}' has User '{entry.user_id}'.")
            for post in posts:
                if entry.user_id == post.user_id and post.type == challenge.type:
                    print(f"User {post.user_id} has posted {post.name}.")

if __name__ == "__main__":
    app.run()