from django.contrib import admin

from listimoveis.imoveis.models import Imovel


class ImovelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'address', 'cep']
    search_fields = ('name', 'address', 'cep')
    readonly_fields = ('name', 'slug', 'address', 'cep', 'photo', 'description')

    def photo_img(self, obj):
        return '<img width="150px" height="150px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Imovel, ImovelModelAdmin)
