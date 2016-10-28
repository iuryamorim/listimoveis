from django.db import models
from django.shortcuts import resolve_url as r
from django.utils.safestring import mark_safe

from listimoveis.imoveis.validators import validate_cep


class Imovel(models.Model):
    name = models.CharField('nome', max_length=255)
    address = models.CharField('endereço', max_length=255)
    cep = models.CharField('cep', validators=[validate_cep], max_length=8)
    slug = models.SlugField('slug')
    photo = models.ImageField('foto', upload_to='imovel/%m%d%y%H%M%S/')
    description = models.TextField('descrição', blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add = True)

    class Meta:
        verbose_name_plural = 'imóveis'
        verbose_name = 'imóvel'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo.url))
    image_tag.short_description = 'Foto'