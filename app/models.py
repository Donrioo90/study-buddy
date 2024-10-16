from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Define relationships
    study_groups = db.relationship('UserGroup', back_populates='user')

class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120), nullable=False)

    # Define relationships
    posts = db.relationship('Post', back_populates='study_group')
    members = db.relationship('UserGroup', back_populates='study_group')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    study_group_id = db.Column(db.Integer, db.ForeignKey('study_group.id'))
    
    # Define relationships
    study_group = db.relationship('StudyGroup', back_populates='posts')

class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    study_group_id = db.Column(db.Integer, db.ForeignKey('study_group.id'))
    
    # Define relationships
    user = db.relationship('User', back_populates='study_groups')
    study_group = db.relationship('StudyGroup', back_populates='members')
