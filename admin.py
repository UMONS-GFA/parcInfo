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
    pass


class GraphicCardAdmin(admin.ModelAdmin):
    pass


class HardDriveAdmin(admin.ModelAdmin):
    pass


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name')


class DesktopAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name', 'ref_processor', 'memory_size', 'ref_graphic_card', 'ref_hard_drive',
                    'ref_localisation', 'serial')
    fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'ref_graphic_card', 'ref_hard_drive',
              'ref_localisation', 'usage_note')


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'name', 'ref_processor', 'memory_size', 'ref_graphic_card', 'ref_hard_drive',
                    'ref_localisation', 'serial')
    fields = ('serial', 'name', 'ref_user', 'ref_processor', 'memory_size', 'ref_graphic_card', 'ref_hard_drive',
              'ref_localisation', 'usage_note')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'ref_localisation')
    inlines = (CnxServerProcessorInline, CnxServerGraphicCardInline, CnxServerHardDriveInline,)

admin.site.register(Processor, ProcessorAdmin)
admin.site.register(GraphicCard)
admin.site.register(HardDrive)
admin.site.register(Localisation)
#admin.site.register(Computer, ComputerAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Server, ServerAdmin)
