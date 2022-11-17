from playhouse.db_url import connect
from peewee import Model
from peewee import CharField

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()


class Post(Model):
    name = CharField()
    title = CharField()
    body = CharField()

    class Meta:
        database = db
        table_name = "post"


db.create_tables([Post])
