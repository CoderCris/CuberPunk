from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

# Create an engine that stores data in the local directory's sqlite database file
engine = create_engine('sqlite:///mydatabase.db' )

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create a new user and add it to the session
new_user = User(name="John Doe", email="john.doe@example.com")
session.add(new_user)

# Commit the session to write the data to the database
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
