from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    #  password = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    #  @staticmethod
    #  def make_unique_username(username):
    #      if User.query.filter_by(username=username).first() is None:
    #          return username
    #      version = 2
    #      while True:
    #          new_username = username + str(version)
    #          if User.query.filter_by(username=new_username).first() is None:
    #              break
    #          version += 1
    #      return new_username 

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
