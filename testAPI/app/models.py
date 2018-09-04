from app import db

class User(db.modle):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.string(80),unique=True)
    email = db.Column(db.string(320),unique=True)
    password = db.Column(db.string(32),nullable=False)

    def __repr__(self):
        return f'<Usre {self.username}>'

