from sqlalchemy import *
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
# meta.create_all(engine)

conn = engine.connect()

"""
# Insertion of data

ins = students.insert()
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
result = conn.execute(ins)
conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])

"""
# pragma table_info('students');  # View table info in sqlite viewer

s = students.select()
result = conn.execute(s)

# Using Text to Fetch
t = text("select * from students")
result = conn.execute(t)

print(result.fetchall()) # [(1, 'Ravi', 'Kapoor'), (2, 'Ravi', 'Kapoor'), (3, 'Rajiv', 'Khanna'), (4, 'Komal', 'Bhandari'), (5, 'Abdul', 'Sattar'), (6, 'Priya', 'Rajhans')]

