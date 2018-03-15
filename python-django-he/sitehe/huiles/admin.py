# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Famille, Propriete, ProprieteEffective
from models import HuileEssentielle

# Register your models here.


class ProprieteEffectiveInLine(admin.StackedInline):
    """
    ProprieteEffectiveInLine is stacked inline propriete effective for admin
    """
    model = ProprieteEffective
    extra = 1


class HuileEssentielleAdmin(admin.ModelAdmin):
    """
    Admin of huile essentielle
    """
    inlines = [ProprieteEffectiveInLine]


admin.site.register(Famille)
admin.site.register(Propriete)
admin.site.register(HuileEssentielle, HuileEssentielleAdmin)
