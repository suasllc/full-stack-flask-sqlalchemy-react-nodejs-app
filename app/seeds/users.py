from werkzeug.security import generate_password_hash
from app.models import db, User
from faker import Faker
fake = Faker()


# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password', bio='Seeder files are my favorite to make!', websiteUrl="www.google.com",
                name="Klark Kent",profilePicUrl="https://placeimg.com/200/200")
    db.session.add(demo)

    michael = User(username='MichaelJensen24', email='michael@gmail.com',
                password='password', bio='Michael is my name and coding is my game!', websiteUrl="www.google.com",
                name="Michael",profilePicUrl="https://placeimg.com/201/201")
    db.session.add(michael)

    tony = User(username='TonyRox', email='tony@gmail.com',
                password='password', bio='Tony is my name and coding is my game!', websiteUrl="www.google.com",
                name="Tony ",profilePicUrl="https://placeimg.com/202/202")
    db.session.add(tony)

    Daniel = User(username='DanielIzKewl', email='Daniel@gmail.com',
                password='password', bio='Daniel is my name and coding is my game!', websiteUrl="www.google.com",
                name="Daniel ",profilePicUrl="https://placeimg.com/203/203")
    db.session.add(Daniel)

    adam = User(username='AdamDaMan', email='adam@gmail.com',
                password='password', bio='adam is my name and coding is my game!', websiteUrl="www.google.com",
                name="Adam ",profilePicUrl="https://placeimg.com/204/204")
    db.session.add(adam)


    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()
