# Ambientes virtuais em Python (venv)More actions
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
import pymysql.cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="planck14",
    database="mysql",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        sql = "SHOW TABLES;"
        cursor.execute(sql)
        tables = cursor.fetchall()
        for table in tables:
            for key, value in table.items():
                print(value)
        print("-" * 25)