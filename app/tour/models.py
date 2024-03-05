import datetime
from app import db


from slugify import slugify
from sqlalchemy.exc import IntegrityError

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    name_slug = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    price = db.Column(db.Integer)
    bookings = db.relationship('Booking', backref='Tour', lazy=True, cascade='all, delete-orphan', order_by='asc(Booking.datecreated)')

    def __repr__(self):
        return f'<Tour {self.name}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.name_slug:
            self.name_slug = slugify(self.name)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.name_slug = f'{slugify(self.name)}-{count}'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_slug(slug):
        return Tour.query.filter_by(name_slug=slug).first()

    @staticmethod
    def get_all():
        return Tour.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Tour.query.get(id)