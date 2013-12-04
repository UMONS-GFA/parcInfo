__author__ = 'Christophe Bastin'

from django.contrib import admin
from models import *

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name')


class DesktopAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name', 'ref_processor', 'ref_hard_drive')

admin.site.register(Processor)
admin.site.register(GraphicCard)
admin.site.register(HardDrive)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Laptop)
admin.site.register(Server)
