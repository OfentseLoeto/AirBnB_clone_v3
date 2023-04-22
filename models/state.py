#!/usr/bin/python3

Update State: (models/state.py)

State inherits from BaseModel and Base (respect the order)
Add or replace in the class State:
class attribute __tablename__
represents the table name, states
class attribute name
represents a column containing a string (128 characters)
can’t be null
for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
