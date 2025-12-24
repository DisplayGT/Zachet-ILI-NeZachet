from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Preparats(db.Model):
    __tablename__ = 'preparats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    serial = db.Column(db.String(20), nullable=False)
    doze = db.Column(db.String(10), nullable=False)
    count = db.Column(db.String(10), nullable=False)
    registr = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Preparats {self.name}>'


class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(200), nullable=False)
    teacher = db.Column(db.String(200), nullable=False)
    how_many = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Groups {self.group_name}>'


class Kids(db.Model):
    __tablename__ = 'kids'
    id = db.Column(db.Integer, primary_key=True)
    kid = db.Column(db.String(150), nullable=False)
    birth = db.Column(db.String(35), nullable=False)
    groupp = db.Column(db.String(120), nullable=False)
    adress = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(80), nullable=False, default='Не привит')

    def __repr__(self):
        return f'<Kids {self.kid}>'


class Privivki(db.Model):
    __tablename__ = 'privivki'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    preparat = db.Column(db.String(50), nullable=False)
    vacine = db.Column(db.String(40), nullable=False)
    method = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'<Privivki {self.fullname}>'