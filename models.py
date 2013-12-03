from django.db import models
from django.contrib.auth.models import User


class Processor(models.Model):
    id_processor = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.manufacturer + " " + self.type


class GraphicCard(models.Model):
    id_graphic_card = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    memory_size = models.IntegerField()

    def __unicode__(self):
        return self.manufacturer + " " + self.type


class HardDrive(models.Model):
    id_hard_drive = models.AutoField(primary_key=True)
    size = models.IntegerField()
    flash_drive = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.size)


class Computer(models.Model):
    id_computer = models.AutoField(primary_key=True)
    serial = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, unique=True)
    usage_note = models.TextField( blank=True, null=True)
    ref_user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Desktop(Computer):
    ref_processor = models.ForeignKey(Processor)
    ref_hard_drive = models.ForeignKey(HardDrive)


class Laptop(Computer):
    ref_processor = models.ForeignKey(Processor)
    ref_hard_drive = models.ForeignKey(HardDrive)


class Server(Computer):
    ref_processor = models.ManyToManyField(Processor)
    ref_graphic_card = models.ManyToManyField(GraphicCard)
    nb_disk = models.IntegerField(default=1)
    ref_hard_drive = models.ManyToManyField(HardDrive)