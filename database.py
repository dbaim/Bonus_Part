import config
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, create_engine


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


eng = get_engine(config.username, config.pwd, config.hostname, config.port_id, config.database)
base = declarative_base()

Session = sessionmaker(bind=eng)
session = Session()


def init_db():
    filepath = Path('db_init.sql')

    with eng.begin() as conn:
        for query in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(query))

    print('All tables were created successfully')


def fill_mock_db():
    filepath = Path('fill_db.sql')

    with eng.connect() as conn:
        for query in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(query))

    print('All rows were inserted successfully')

init_db()
fill_mock_db()
#
# # Query 1
# def query_1():
#     with eng.connect() as conn:
#         dis = conn.execute(text("""
#         SELECT D.disease_code, D.description
#         FROM disease D, discover S
#         WHERE D.disease_code = S.disease_code AND D.pathogen = 'bacterial' AND S.first_enc_date < '1990-01-01';
#         """)).mappings()
#     print([{column: disease_code[column] for column in dis.keys()} for disease_code in dis])
#
#
# # Query 2
# def query_2():
#     with eng.connect() as conn:
#         doctors = conn.execute(text("""
#         SELECT DISTINCT U.name, U.surname, D.degree
#         FROM users U JOIN doctor D ON U.email = D.email
#         JOIN specialize S ON U.email = S.email
#         JOIN diseasetype N ON S.id = N.id
#         WHERE N.description != 'infectous disease';
#         """)).mappings()
#     print([{column: name[column] for column in doctors.keys()} for name in doctors])
#
#
# # Query 3
# def query_3():
#     with eng.connect() as conn:
#         doctors = conn.execute(text("""
#         SELECT U.name, U.surname, D.degree
#         FROM users U JOIN doctor D ON U.email = D.email
#         FULL JOIN specialize S ON U.email = S.email
#         FULL JOIN diseasetype N ON S.id = N.id
#         GROUP BY U.name, U.surname, D.degree
#         HAVING COUNT(S.id) > 1
#         """)).mappings()
#     print([{column: name[column] for column in doctors.keys()} for name in doctors])
#
#
# # Query 3
# def query_4():
#     with eng.connect() as conn:
#         doctors = conn.execute(text("""
#         SELECT C.cname, U.salary
#         FROM users U JOIN doctor D ON U.email = D.email
#         FULL JOIN country C ON U.cname = C.cname
#         FULL JOIN specialize S ON U.email = S.email
#         FULL JOIN diseasetype N ON S.id = N.id
#         WHERE N.description = 'virology'
#         """)).mappings()
#     print([{column: name[column] for column in doctors.keys()} for name in doctors])
#
#
# # Assuming that all doctors = Public Servants, besides them in the table I have 2 people who did research on covid and
# # thus can be found by the query specification. They both work in special department 11 (D11).
# def query_5():
#     with eng.connect() as conn:
#         doctors = conn.execute(text("""
#         SELECT D.department, D.email
#         FROM publicservant D
#         JOIN record N ON D.email = N.email
#         GROUP BY D.department, D.email
#         HAVING COUNT(N.email) > 1
#         """)).mappings()
#     print([{column: name[column] for column in doctors.keys()} for name in doctors])
#
#
# def query_6():
#     with eng.connect() as conn:
#         doctors = conn.execute(text("""
#         UPDATE users
#         SET salary = salary * 2
#         WHERE (
#         JOIN record N ON D.email = N.email
#         GROUP BY D.department, D.email
#         HAVING COUNT(N.email) > 1
#         """)).mappings()
#     print([{column: name[column] for column in doctors.keys()} for name in doctors])
#
#
# query_1()
# query_2()
# query_3()
# query_4()
# query_5()



