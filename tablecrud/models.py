from django.db import models,connection

# Create your models here.
class Person(models.Model):
    name = models.CharField( max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = 'person'
        app_label = 'tablecrud'

    @classmethod
    def insert_person(cls, name, age):
        with connection.cursor() as cursor:
            cursor.execute("SELECT InsertPerson(%s, %s)", [name, age])