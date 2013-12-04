from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Processor(models.Model):
    id_processor = models.AutoField(primary_key=True)
    manufacturer = models.CharField(verbose_name=_('manufacturer'), max_length=255)
    type_processor = models.CharField(verbose_name=_('type'), max_length=255)

    class Meta:
        verbose_name = _('processor')
        verbose_name_plural = _('processors')

    def __unicode__(self):
        return self.manufacturer + " " + self.type_processor


class GraphicCard(models.Model):
    id_graphic_card = models.AutoField(primary_key=True)
    manufacturer = models.CharField(verbose_name=_('manufacturer'), max_length=255)
    type_graphic_card = models.CharField(verbose_name=_('type'), max_length=255)
    memory_size = models.IntegerField(verbose_name=_('memory size'))

    class Meta:
        verbose_name = _('graphic card')
        verbose_name_plural = _('graphic cards')

    def __unicode__(self):
        return self.manufacturer + " " + self.type_graphic_card


class HardDrive(models.Model):
    id_hard_drive = models.AutoField(primary_key=True)
    size = models.IntegerField(verbose_name=_('size'))
    flash_drive = models.BooleanField(verbose_name=_('ssd'), default=False)

    class Meta:
        verbose_name = _('hard drive')
        verbose_name_plural = _('hard drives')

    def __unicode__(self):
        return str(self.size)


class Computer(models.Model):
    id_computer = models.AutoField(primary_key=True)
    serial = models.IntegerField(verbose_name=_('serial_number'), unique=True)
    name = models.CharField(verbose_name=_('name'), max_length=255, unique=True)
    usage_note = models.TextField(verbose_name=_('usage note'), blank=True, null=True)
    ref_user = models.ForeignKey(User, verbose_name=_('user'))

    class Meta:
        verbose_name = _('computer')
        verbose_name_plural = _('computers')

    def __unicode__(self):
        return self.name


class Desktop(Computer):
    ref_processor = models.ForeignKey(Processor, verbose_name=_('processor'))
    ref_hard_drive = models.ForeignKey(HardDrive, verbose_name=_('hard drive'))

    class Meta:
        verbose_name = _('desktop')
        verbose_name_plural = _('desktops')


class Laptop(Computer):
    ref_processor = models.ForeignKey(Processor, verbose_name=_('processor'))
    ref_hard_drive = models.ForeignKey(HardDrive, verbose_name=_('hard drive'))

    class Meta:
        verbose_name = _('laptop')
        verbose_name_plural = _('laptops')


class Server(Computer):
    ref_processor = models.ManyToManyField(Processor, verbose_name=_('processor'))
    ref_graphic_card = models.ManyToManyField(GraphicCard, verbose_name=_('graphic card'))
    nb_disk = models.IntegerField(default=1, verbose_name=_('number of disk'))
    ref_hard_drive = models.ManyToManyField(HardDrive, verbose_name=_('hard drive'))

    class Meta:
        verbose_name = _('server')
        verbose_name_plural = _('servers')