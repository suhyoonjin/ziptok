from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=24, null=False, primary_key=True)
    pwd = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    birth = models.CharField(max_length=7, null=False)
    email = models.CharField(max_length=50, null=False)
    phone_num = models.CharField(max_length=10, null=False)
    addr = models.CharField(max_length=50)
    rcmd_id = models.CharField(max_length=24, null=True)
    category = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "User"


class Expert(models.Model):
    id = models.CharField(max_length=24, null=False, primary_key=True)
    isExpert = models.CharField(max_length=10, null = False)
    job = models.CharField(max_length=24, null=False)
    off_name = models.CharField(max_length=30, null=False)
    off_addr = models.CharField(max_length=30, null=False)
    off_tel = models.CharField(max_length=30, null=False)
    off_start_year = models.CharField(max_length=4)
    field = models.CharField(max_length=20, null=False)
    hist = models.CharField(max_length=20, null=False)
    reg = models.CharField(max_length=20, null=False)
    short_intro = models.CharField(max_length=100, null=False)
    long_intro = models.CharField(max_length=500, null=False)
    photo = models.ImageField(null=False)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'Expert'



