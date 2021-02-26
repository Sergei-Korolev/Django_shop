from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *


class NotebookAdmin(admin.ModelAdmin):

    def formfiel_for_foreignkey(self, db_field, request, **kwargs):
        if db.db_field.name == 'category':
            return ModelChoiceField(Category.object.filter(slug='notebooks'))
        return super().formfiel_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfiel_for_foreignkey(self, db_field, request, **kwargs):
        if db.db_field.name == 'category':
            return ModelChoiceField(Category.object.filter(slug='smartphones'))
        return super().formfiel_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
