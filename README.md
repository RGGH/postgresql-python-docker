# Postgresql (Docker container) + Python

This is a ready made framework to begin a Python & SQL project

Uses .sql and .yml to create a database, create tables, add dummy data

---

- Clone the repo, 
- issue "docker-compose build" 
- run app2.py or write your own python code
-  the data will be persistent as it uses a mounted volume

---

### Python + Psycopg2

  Psycopg2 : use this: (rather than pip install psycpog2)
  pip install psycopg2-binary
  
  https://pypi.org/project/psycopg2-binary/
  
  Psycopg 2 is mostly implemented in C as a libpq wrapper, 
  resulting in being both efficient and secure.
