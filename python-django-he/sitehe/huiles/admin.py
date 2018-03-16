# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# INLINE ADMINS


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


class CaracteriologieInLine(admin.StackedInline):
    """
    Ajout de source en ligne
    """
    model = Caracteriologie
    extra = 1


class ProprieteMaladieInLine(admin.StackedInline):
    """
    Ajout de propriétés associées à une maladie
    """
    model = ProprieteMaladie
    extra = 1


class ContreIndicationMaladieInLine(admin.StackedInline):
    """
    Ajout des contre-indications associées à une maladie
    """
    model = ContreIndicationMaladie
    extra = 1


# SPECIFIC ADMIN WITH INLINES

class HuileEssentielleAdmin(admin.ModelAdmin):
    """
    Admin of huile essentielle
    """
    inlines = [ProprieteEffectiveInLine, ContreIndicationInLine, SourceInLine, CaracteriologieInLine]


class MaladieAdmin(admin.ModelAdmin):
    """
    Admin of Maladie
    """
    inlines = [ProprieteMaladieInLine, ContreIndicationMaladieInLine]


# REGISTERING


admin.site.register(Famille)
admin.site.register(Propriete)
admin.site.register(ContreIndication)
admin.site.register(Source)
admin.site.register(Caracteriologie)
admin.site.register(HuileEssentielle, HuileEssentielleAdmin)
admin.site.register(Maladie, MaladieAdmin)
