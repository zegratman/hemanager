# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Famille(models.Model):
    """
    Familles
    """
    nom = models.CharField(max_length=255, primary_key=True, verbose_name="Famille")
    description = models.TextField(blank=True, verbose_name="Description", null=True)

    def __unicode__(self):
        return unicode(self.nom)

    def __str__(self):
        return self.__unicode__()


class Propriete(models.Model):
    """
    Proprietes
    """
    nom = models.CharField(max_length=255, primary_key=True, verbose_name="Propriété")
    description = models.TextField(blank=True, verbose_name="Description")

    def __unicode__(self):
        return unicode(self.nom)

    def __str__(self):
        return self.__unicode__()


class ContreIndication(models.Model):
    """
    ContreIndication
    """
    nom = models.CharField(max_length=255, primary_key=True, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    def __unicode__(self):
        return unicode(self.nom)

    def __str__(self):
        return self.__unicode__()


class Source(models.Model):
    """
    Source
    """
    nom = models.CharField(max_length=255, primary_key=True, verbose_name="Nom")
    auteur = models.CharField(max_length=255, verbose_name="Auteur")
    year = models.IntegerField(verbose_name="Année")

    def __unicode__(self):
        return unicode(self.nom) + " (" + unicode(self.auteur) + ")[" + unicode(self.year) + "]"

    def __str__(self):
        return self.__unicode__()


class Maladie(models.Model):
    """
    Maladie
    """
    nom = models.CharField(max_length=255, primary_key=True, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    def __unicode__(self):
        return unicode(self.nom)

    def __str__(self):
        return self.__unicode__()


class HuileEssentielle(models.Model):
    """
    Huile essentielle
    """
    qtte_choices = (
        (2, '2 mL'),
        (5, '5 mL'),
        (10, '10 mL'),
        (15, '15 mL'),
        (20, '20 mL'),
        (30, '30 mL'),
    )
    """
    Champs
    """
    nom = models.CharField(max_length=255, primary_key=True, blank=False, verbose_name="Nom", db_index=True)
    nom_alternatif = models.CharField(max_length=255, verbose_name="Nom alternatif", blank=True)

    prix = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Prix", blank=True, default=0.00)
    quantite = models.IntegerField(choices=qtte_choices, verbose_name="Quantité", blank=True,
                                   default=qtte_choices.__getitem__(2))

    prix_bio = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Prix bio", blank=True, default=0.00)
    quantite_bio = models.IntegerField(choices=qtte_choices, verbose_name="Quantité bio", blank=True,
                                       default=qtte_choices.__getitem__(2))

    schema = models.ImageField(verbose_name="Schéma", blank=True)

    famille_1 = models.ForeignKey(Famille, on_delete=models.CASCADE, blank=False, verbose_name="Famille primaire",
                                  related_name="+")
    famille_2 = models.ForeignKey(Famille, on_delete=models.CASCADE, verbose_name="Famille secondaire", blank=True,
                                  related_name="+", null=True)
    famille_3 = models.ForeignKey(Famille, on_delete=models.CASCADE, verbose_name="Famille tertiaire", blank=True,
                                  related_name="+", null=True)
    famille_4 = models.ForeignKey(Famille, on_delete=models.CASCADE, verbose_name="Famille annexe 1", blank=True,
                                  related_name="+", null=True)
    famille_5 = models.ForeignKey(Famille, on_delete=models.CASCADE, verbose_name="Famille annexe 2", blank=True,
                                  related_name="+", null=True)

    notes = models.TextField(verbose_name="Notes", blank=True)

    def __unicode__(self):
        return unicode(self.nom)

    def __str__(self):
        return self.__unicode__()


class ProprieteEffective(models.Model):
    """
    Propriété effective d'une huile essentielle
    """
    nom_prop = models.ForeignKey(Propriete, on_delete=models.CASCADE, related_name="+")
    nom_he = models.ForeignKey(HuileEssentielle, on_delete=models.CASCADE, related_name="+")
    efficacite_possible = (
        ("+", "+"),
        ("++", "++"),
        ("+++", "+++"),
        ("++++", "++++"),
        ("+++++", "++++++"),
        ("tout ou rien", "tout ou rien")
    )
    efficacite = models.CharField(max_length=31, verbose_name="Efficacité", choices=efficacite_possible)

    def __unicode__(self):
        return unicode(self.nom_prop) + " [" + unicode(self.efficacite) + "]"

    def __str__(self):
        return self.__unicode__()


class ContreIndicationHE(models.Model):
    """
    Contre indication d'une huile essentielle
    """
    nom_contre_indication = models.ForeignKey(ContreIndication, on_delete=models.CASCADE, related_name="+")
    nom_he = models.ForeignKey(HuileEssentielle, on_delete=models.CASCADE, related_name="+")

    def __unicode__(self):
        return unicode(self.nom_he) + " > " + unicode(self.nom_contre_indication)

    def __str__(self):
        return self.__unicode__()


class SourceHE(models.Model):
    """
    Source associée à une huile essentielle
    """
    nom_source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="+")
    nom_he = models.ForeignKey(HuileEssentielle, on_delete=models.CASCADE, related_name="+")
    pages = models.CharField(max_length=255, verbose_name="Pages")

    def __unicode__(self):
        return unicode(self.nom_he) + " > " + unicode(self.nom_source)

    def __str__(self):
        return self.__unicode__()


class Caracteriologie(models.Model):
    """
    ContreIndication
    """
    identifier = models.IntegerField(verbose_name="ID", primary_key=True, auto_created=True)
    description = models.TextField(blank=True, verbose_name="Description")
    huile_essentielle = models.ForeignKey(HuileEssentielle, on_delete=models.CASCADE, related_name="+")

    def __unicode__(self):
        return unicode(self.identifier)

    def __str__(self):
        return self.__unicode__()


class ProprieteMaladie(models.Model):
    """
    proprietes associées à une maladie
    """
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE, related_name="+")
    maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE, related_name="+")

    def __unicode__(self):
        return unicode(self.maladie) + " > " + unicode(self.propriete)

    def __str__(self):
        return self.__unicode__()


class ContreIndicationMaladie(models.Model):
    """
    Contre-indications associées à une maladie
    """
    contre_indication = models.ForeignKey(ContreIndication, on_delete=models.CASCADE, related_name="+")
    maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE, related_name="+")

    def __unicode__(self):
        return unicode(self.maladie) + " > " + unicode(self.contre_indication)

    def __str__(self):
        return self.__unicode__()
