from django.contrib import admin

from listimoveis.imoveis.models import Imovel


class ImovelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'address', 'cep']
    search_fields = ('name', 'address', 'cep')
    readonly_fields = ('name', 'slug', 'address', 'cep', 'photo', 'description')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Imovel, ImovelModelAdmin)
