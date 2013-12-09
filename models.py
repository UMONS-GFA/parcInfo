from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# connection models

class CnxServerProcessor(models.Model):
    id_cnx_server_processor = models.AutoField(primary_key=True)
    ref_server = models.ForeignKey('Server')
    ref_processor = models.ForeignKey('Processor')
    nbr_processor = models.IntegerField(verbose_name=_('number of processors'), default=1)

    class Meta:
        verbose_name = _('processor')
        verbose_name_plural = _('processors')


class CnxServerGraphicCard(models.Model):
    id_cnx_server_graphicCard = models.AutoField(primary_key=True)
    ref_server = models.ForeignKey('Server')
    ref_graphic_card = models.ForeignKey('GraphicCard')
    nbr_graphic_card = models.IntegerField(verbose_name=_('number of graphic cards'), default=1)

    class Meta:
        verbose_name = _('graphic card')
        verbose_name_plural = _('graphic cards')


class CnxServerHardDrive(models.Model):
    id_cnx_server_hardDrive = models.AutoField(primary_key=True)
    ref_server = models.ForeignKey('Server')
    ref_hard_drive = models.ForeignKey('HardDrive')
    nbr_hard_drive = models.IntegerField(verbose_name=_('number of hard drive'), default=1)

    class Meta:
        verbose_name = _('hard drive')
        verbose_name_plural = _('hard drives')
# end of connection models


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
    memory_size = models.IntegerField(verbose_name=_('memory size'), help_text=_('in MB'), blank=True, null=True)

    class Meta:
        verbose_name = _('graphic card')
        verbose_name_plural = _('graphic cards')

    def __unicode__(self):
        return self.manufacturer + " " + self.type_graphic_card


class HardDrive(models.Model):
    id_hard_drive = models.AutoField(primary_key=True)
    size = models.IntegerField(verbose_name=_('size'), help_text=_('in GB'))
    flash_drive = models.BooleanField(verbose_name=_('ssd'), default=False)

    class Meta:
        verbose_name = _('hard drive')
        verbose_name_plural = _('hard drives')

    def __unicode__(self):
        return str(self.size)


class Localisation(models.Model):
    id_localisation = models.AutoField(primary_key=True)
    localisation_name = models.CharField(max_length=255, verbose_name=_('localisation name'))

    class Meta:
        verbose_name = _('localisation')
        verbose_name_plural = _('localisations')

    def __unicode__(self):
        return self.localisation_name


class Computer(models.Model):
    id_computer = models.AutoField(primary_key=True)
    serial = models.IntegerField(verbose_name=_('serial_number'), unique=True)
    name = models.CharField(verbose_name=_('name'), max_length=255, blank=True, null=True)
    usage_note = models.TextField(verbose_name=_('usage note'), blank=True, null=True)
    memory_size = models.IntegerField(verbose_name=_('memory size'), help_text=_('in MB'))
    ref_user = models.ForeignKey(User, verbose_name=_('user'))
    localisation = models.ForeignKey(Localisation, verbose_name=_('localisation'))

    class Meta:
        verbose_name = _('computer')
        verbose_name_plural = _('computers')

    def __unicode__(self):
        return self.name


class Desktop(Computer):
    ref_processor = models.ForeignKey(Processor, verbose_name=_('processor'))
    ref_graphic_card = models.ForeignKey(GraphicCard, verbose_name=_('graphic card'))
    ref_hard_drive = models.ForeignKey(HardDrive, verbose_name=_('hard drive'), help_text=_('in GB'))

    class Meta:
        verbose_name = _('desktop')
        verbose_name_plural = _('desktops')


class Laptop(Computer):
    ref_processor = models.ForeignKey(Processor, verbose_name=_('processor'))
    ref_graphic_card = models.ForeignKey(GraphicCard, verbose_name=_('graphic card'))
    ref_hard_drive = models.ForeignKey(HardDrive, verbose_name=_('hard drive'), help_text=_('in GB'))

    class Meta:
        verbose_name = _('laptop')
        verbose_name_plural = _('laptops')


class Server(Computer):
    ref_processor = models.ManyToManyField(Processor, through='CnxServerProcessor', verbose_name=_('processor'))
    ref_graphic_card = models.ManyToManyField(GraphicCard, through='CnxServerGraphicCard',
                                              verbose_name=_('graphic card'))
    ref_hard_drive = models.ManyToManyField(HardDrive, through='CnxServerHardDrive', verbose_name=_('hard drive'),
                                            help_text=_('in GB'))

    class Meta:
        verbose_name = _('server')
        verbose_name_plural = _('servers')