from datetime import date
from app import db




class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user_name = db.Column(db.String)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id', ondelete='SET NULL'), nullable=False)
    tour_name=db.Column(db.String)
    people = db.Column(db.Integer)
    datecreated = db.Column(db.DateTime, default=date.today)


    def __init__(self,people=people, tour_name=None, user_id=None, user_name=user_name, tour_id=None):
        self.user_id = user_id
        self.user_name = user_name
        self.tour_id = tour_id
        self.tour_name=tour_name
        self.people= people

    def __repr__(self):
        return f'<Booking {self.tour_name}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id):
        return Booking.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_by_id(id):
        return Booking.query.get(id)