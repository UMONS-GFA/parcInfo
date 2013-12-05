__author__ = 'Christophe Bastin'

from django.contrib import admin
from models import *


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name')


class DesktopAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name', 'ref_processor', 'memory_size', 'ref_hard_drive', 'serial')
    fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'ref_hard_drive', 'localisation',
              'usage_note')


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name', 'ref_processor', 'memory_size', 'ref_hard_drive', 'serial')
    fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'ref_hard_drive', 'localisation',
              'usage_note')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial')
    fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'nb_disk', 'ref_hard_drive',
              'localisation', 'usage_note')

admin.site.register(Processor)
admin.site.register(GraphicCard)
admin.site.register(HardDrive)
admin.site.register(Localisation)
#admin.site.register(Computer, ComputerAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Server, ServerAdmin)
