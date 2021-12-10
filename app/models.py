from config import db

class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=False, unique=True, nullable=False)
    firstName = db.Column(db.String(50), index=False, unique=False, nullable=True)
    lastName = db.Column(db.String(100), index=False, unique=False, nullable=True)
    password = db.Column(db.String(40), nullable=False)
    
    def __str__(self):
        return f"{self.username}, {self.id}"

    def __repr__(self):
        return '<User {}>'.format(self.username)
