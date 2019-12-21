from main import app, db, User


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


'''
export FLASK_APP=manage.py
flask shell
>>> db.create_all()
>>> user = User(username="忘返")
>>> db.session.add(user)
>>> db.session.commit()

>>> users = User.query.all()
>>> users
[User 忘返]

>>> users = User.query.limit(10).all()
# ascending
>>> users = User.query.order_by(User.username).all()
# descending
>>> users = User.query.order_by(User.username.desc()).all()

>>> user = User.query.first()
>>> user.username
fake_name

#by id
>>> user = User.query.get(1)
>>> user.username
fake_name

#The first() and all() methods return a value, and therefore end the chain.
>>> users = User.query.order_by(
    User.username.desc()
).limit(10).first()

>>> page = User.query.paginate(1, 10)
# returns the entities in the page
>>> page.items
[User 忘返]

# what page does this object represent
>>> page.page
1
# How many pages are there
>>> page.pages
1
# are there enough models to make the next or previous page
>>> page.has_prev, page.has_next
(False, False)

# return the next or previous page pagination object
# if one does not exist returns the current page
>>> page.prev(), page.next()

>>> users = User.query.filter_by(username='fake_name').all()

>>> user = User.query.filter(
    User.id > 1
).all()

'''
