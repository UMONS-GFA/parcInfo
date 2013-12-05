__author__ = 'Christophe Bastin'

from django.contrib import admin
from models import *

class CnxServerProcessorInline(admin.TabularInline):
    model = CnxServerProcessor
    extra = 1


class CnxServerGraphicCardInline(admin.TabularInline):
    model = CnxServerGraphicCard
    extra = 1


class CnxServerHardDriveInline(admin.TabularInline):
    model = CnxServerHardDrive
    extra = 1


class ProcessorAdmin(admin.ModelAdmin):
    inlines = (CnxServerProcessorInline,)


class GraphicCardAdmin(admin.ModelAdmin):
    inlines = (CnxServerGraphicCardInline,)


class HardDriveAdmin(admin.ModelAdmin):
    inlines = (CnxServerHardDriveInline,)


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
    inlines = (CnxServerProcessorInline, CnxServerGraphicCardInline,CnxServerHardDriveInline,)
    #fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'nb_disk', 'ref_hard_drive',
    #          'localisation', 'usage_note')

admin.site.register(Processor, ProcessorAdmin)
admin.site.register(GraphicCard)
admin.site.register(HardDrive)
admin.site.register(Localisation)
#admin.site.register(Computer, ComputerAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Server, ServerAdmin)
