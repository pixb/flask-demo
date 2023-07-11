from . import db

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)

	def __repr__(self):
		return '<User %r>' % self.username

class VideoInfo(db.Model):
    __tablename__='video_info'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    videoid=db.Column(db.Integer)
    title=db.Column(db.String(1024),unique=True)

    def __repr__(self):
        return '<VideoInfo %r>' % self.videoid
