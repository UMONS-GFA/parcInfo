__author__ = 'Christophe Bastin'

from django.contrib import admin
from models import *


admin.site.register(Processor)
admin.site.register(GraphicCard)
admin.site.register(HardDrive)
admin.site.register(Desktop)
admin.site.register(Laptop)
admin.site.register(Server)
