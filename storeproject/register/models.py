from django.db import models


class DepartmentModel(models.Model):
    Did=models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=100)

    class Meta:
        db_table = "department"


class CourseModel(models.Model):
    Cid = models.IntegerField(primary_key=True)
    Cname = models.CharField(max_length=100)
    Did=models.IntegerField()


    class Meta:
        db_table = "course"