from django.contrib import admin

# Register your models here.
from blog.models import Entrada, Categoria, Mensajes, Contacto

admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Mensajes)
admin.site.register(Contacto)