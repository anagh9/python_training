"""
Inserting data into the database is a three step process:
> Create the Python object
> Add it to the session
> Commit the session
"""

"""
from yourapp import User
me = User('admin', 'admin@example.com')
db.session.add(me)
db.session.commit()

Deleting records is very similar, instead of add() use delete():
db.session.delete(me)
db.session.commit()
"""

"""
Querying Records

User.query.filter_by(username='peter').first()
User.query.filter_by(username='missing').first()
User.query.filter(User.email.endswith('@example.com')).all()
User.query.order_by(User.username).all()

# Limiting users:
User.query.limit(1).all()

# Get from primary key
User.query.get(1)

# Querying in Views
User.query.filter_by(username=username).first_or_404()
User.query.filter_by(username=username).get_or_404()

# Pagination in FlaskSqlalchemy

from flask_sqlalchemy import Pagination
Page = User.query.paginate(1, 10, False)
Page.items
Page.has_next
Page.has_prev
Page.next_num
Page.prev_num
Page.pages
Page.iter_pages()


# Abort With Mmessage

User.query.filter_by(username=username).first_or_404(description='There is no data with {}'.format(username))
User.query.filter_by(username=username).get_or_404(description='There is no data with {}'.format(username))

"""

