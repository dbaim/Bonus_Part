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


def create_db():
    filepath = Path('db_init.sql')

    with eng.begin() as conn:
        for q in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(q))

    print('Tables created')


def fill_db():
    filepath = Path('fill_db.sql')

    with eng.connect() as conn:
        for q in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(q))

    print('Tables are filled \n')


create_db()
fill_db()


def query_1():
    with eng.connect() as conn:
        dis = conn.execute(text("""
        SELECT D.disease_code, D.description
        FROM disease D, discover S
        WHERE D.disease_code = S.disease_code AND D.pathogen = 'bacterial' AND S.first_enc_date < '1990-01-01';
        """)).mappings()
    print('Query 1:')
    print('\n')
    for k in dis:
        print(k)
    print('\n')


def query_2():
    with eng.connect() as conn:
        doctors = conn.execute(text("""
        SELECT DISTINCT U.name, U.surname, D.degree
        FROM users U JOIN doctor D ON U.email = D.email
        JOIN specialize S ON U.email = S.email
        JOIN diseasetype N ON S.id = N.id
        WHERE N.description != 'infectous disease';
        """)).mappings()
    print('Query 2:')
    print('\n')
    for i in doctors:
        print(i)
    print('\n')


def query_3():
    with eng.connect() as conn:
        doctors = conn.execute(text("""
        SELECT U.name, U.surname, D.degree
        FROM users U JOIN doctor D ON U.email = D.email
        FULL JOIN specialize S ON U.email = S.email
        FULL JOIN diseasetype N ON S.id = N.id
        GROUP BY U.name, U.surname, D.degree
        HAVING COUNT(S.id) > 1
        """)).mappings()
    print('Query 3:')
    print('\n')
    for i in doctors:
        print(i)
    print('\n')


def query_4():
    with eng.connect() as conn:
        doctors = conn.execute(text("""
        SELECT C.cname, U.salary
        FROM users U JOIN doctor D ON U.email = D.email
        FULL JOIN country C ON U.cname = C.cname
        FULL JOIN specialize S ON U.email = S.email
        FULL JOIN diseasetype N ON S.id = N.id
        WHERE N.description = 'virology'
        """)).mappings()
    print('Query 4:')
    print('\n')
    for i in doctors:
        print(i)
    print('\n')


# Assuming that all doctors = Public Servants, besides them in the table I have 2 people who did research on covid and
# thus can be found by the query specification. They both work in special department 11 (D11).
def query_5():
    with eng.connect() as conn:
        doctors = conn.execute(text("""
        SELECT DISTINCT D.department, COUNT(D.email)
        FROM publicservant D
        JOIN record N ON D.email = N.email
        GROUP BY D.department, D.email 
        HAVING COUNT(D.email) > 1
        """)).mappings()
    print('Query 5:')
    print('\n')
    for i in doctors:
        print(i)
    print('\n')


def query_6():
    with eng.connect() as conn:
        conn.execute(text("""
        UPDATE users U
        SET salary = salary * 2
        WHERE U.email IN (
        SELECT R.email
        FROM record R
        GROUP BY R.email
        HAVING COUNT(R.email) > 3)
        """))
    print('Query 6 has been executed \n')


def query_7():
    with eng.connect() as conn:
        conn.execute(text("""
        DELETE FROM users WHERE name LIKE '%bek'
        OR name like '%bek%'
        OR name like 'bek%';

        DELETE FROM users WHERE name LIKE '%Bek'
        OR name like '%Bek%'
        OR name like 'Bek%';

        DELETE FROM users WHERE name LIKE '%Gul'
        OR name like '%Gul%'
        OR name like 'Gul%';

        DELETE FROM users WHERE name LIKE '%gul'
        OR name like '%gul%'
        OR name like 'gul%';
        """))
    print('Query 7 has been executed \n')


def query_8():
    with eng.connect() as conn:
        conn.execute(text("""
        CREATE UNIQUE INDEX idx_pathogen
        ON disease (pathogen);
        """))
    print('Query 8 has been executed \n')


def query_9():
    with eng.connect() as conn:
        servants = conn.execute(text("""
        SELECT R.email, U.name, D.department
        FROM record R JOIN publicservant D ON R.email = D.email JOIN users U ON U.email = D.email
        GROUP BY U.name, D.department, R.email
        HAVING SUM(R.total_patients) > 100000 AND SUM(R.total_patients) < 9999999
        """)).mappings()
    print('Query 9:')
    print('\n')
    for i in servants:
        print(i)
    print('\n')


def query_10():
    with eng.connect() as conn:
        countries = conn.execute(text("""
        SELECT cname, total_patients
        FROM record
        ORDER BY total_patients DESC
        LIMIT 5
        """)).mappings()
    print('Query 10:')
    print('\n')
    for i in countries:
        print(i)
    print('\n')


def query_11():
    with eng.connect() as conn:
        diseases = conn.execute(text("""
        SELECT N.description, SUM(R.total_patients)
        FROM record R JOIN disease D ON R.disease_code = D.disease_code JOIN diseasetype N ON N.id = D.id
        GROUP BY N.description
        """)).mappings()
    print('Query 11:')
    print('\n')
    for i in diseases:
        print(i)
    print('\n')


query_1()
query_2()
query_3()
query_4()
query_5()
query_6()
query_7()
query_8()
query_9()
query_10()
query_11()



