# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


# Register your models here.


class ProprieteEffectiveInLine(admin.StackedInline):
    """
    ProprieteEffectiveInLine is stacked inline propriete effective for admin
    """
    model = ProprieteEffective
    extra = 1


class ContreIndicationInLine(admin.StackedInline):
    """
    Ajout de contre-indications en ligne
    """
    model = ContreIndicationHE
    extra = 1


class SourceInLine(admin.StackedInline):
    """
    Ajout de source en ligne
    """
    model = SourceHE
    extra = 1


class HuileEssentielleAdmin(admin.ModelAdmin):
    """
    Admin of huile essentielle
    """
    inlines = [ProprieteEffectiveInLine, ContreIndicationInLine, SourceInLine]


admin.site.register(Famille)
admin.site.register(Propriete)
admin.site.register(ContreIndication)
admin.site.register(Source)
admin.site.register(HuileEssentielle, HuileEssentielleAdmin)
