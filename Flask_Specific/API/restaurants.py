from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


class Restaurants(db.Model):
    __tablename__ = 'restaurants'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    chef_name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price_range = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    website = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'chef_name': self.chef_name, 'location': self.location, 'category': self.category, 'price_range': self.price_range, 'rating': self.rating, 'address': self.address, 'phone': self.phone, 'website': self.website, 'email': self.email}

    def add_restaurant(_name,_chef_name,_location,_category,_price_range,_rating,_address,_phone,_website,_email):
        new_restaurant = Restaurants(name=_name, chef_name=_chef_name, location=_location, category=_category, price_range=_price_range, rating=_rating, address=_address, phone=_phone, website=_website, email=_email)

        db.session.add(new_restaurant)
        db.session.commit()

    def get_all_restaurants():
        return [Restaurants.json(restaurant) for restaurant in Restaurants.query.all()]

    def get_restaurant(id):
        return Restaurants.json(Restaurants.query.filter_by(id=id).first())

    def update_restaurant(id,_name,_chef_name,_location,_category,_price_range,_rating,_address,_phone,_website,_email):
        restaurant = Restaurants.query.filter_by(id=id).first()

        if restaurant:
            restaurant.name = _name
            restaurant.chef_name = _chef_name
            restaurant.location = _location
            restaurant.category = _category
            restaurant.price_range = _price_range
            restaurant.rating = _rating
            restaurant.address = _address
            restaurant.phone = _phone
            restaurant.website = _website
            restaurant.email = _email

            db.session.commit()
            return restaurant.json()
        return {'message': 'No restaurant found!'}

    def delete_restaurant(id):
        restaurant = Restaurants.query.filter_by(id=id).first()

        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return {'message': 'Restaurant deleted!'}
        return {'message': 'No restaurant found!'}


    
