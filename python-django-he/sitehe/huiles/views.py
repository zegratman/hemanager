# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from models import HuileEssentielle, ContreIndication, ContreIndicationHE, ProprieteEffective, Propriete, Famille


# Create your views here.


def remove_ci_from(filtering, filtered_list):
    """
    Remove the HE using filtering based on CI
    :param filtering: the filtering
    :param filtered_list:  the current HE list
    :return: the updated filtered list
    """
    if 'contre_indic' in filtering and filtering.get('contre_indic') != 'none':
        to_be_excluded_list = ContreIndicationHE.objects.filter(
            nom_contre_indication__in=filtering.getlist('contre_indic'))
        for excluded in to_be_excluded_list:
            if excluded.nom_he_id in filtered_list:
                filtered_list.remove(excluded.nom_he_id)
    return filtered_list


def remove_props_from(filtering, filtered_list):
    """
    Remove the HEs using filtering based on properties
    :param filtering: the filtering
    :param filtered_list: the current HE list
    :return: the updated filtered list
    """
    if 'property' in filtering and filtering.get('property') != 'none':
        filtered_list = [he for he in filtered_list if
                         len(ProprieteEffective.objects.filter(nom_he__exact=he).filter(
                             nom_prop__exact=filtering.get('property'))) > 0]
    return filtered_list


def remove_families_from(filtering, filtered_list):
    """
    Remove the HEs using filtering based on families
    :param filtering: the filtering
    :param filtered_list: the current HE list
    :return: the updated filtered list
    """
    if 'family' in filtering and filtering.get('family') != 'none':
        to_be_excluded_list = []
        families_attr = ['famille_{0}'.format(i) for i in range(1, 6)]
        for he_nom in filtered_list:
            he = HuileEssentielle.objects.get(pk=he_nom)
            families = []
            for attr in families_attr:
                he_famille = getattr(he, attr)
                if he_famille is not None:
                    families.append(he_famille.nom)
            if filtering.get('family') not in families:
                to_be_excluded_list.append(he_nom)
        for excluded in to_be_excluded_list:
            filtered_list.remove(excluded)
    return filtered_list


def he_view(request):
    """
    Main view
    :param request: the request
    :type request: HttpRequest
    :return:
    """

    # Base objects
    he_list = HuileEssentielle.objects.all()
    ci_list = ContreIndication.objects.all()
    prop_list = Propriete.objects.all()
    famille_list = Famille.objects.all()

    # Effective properties
    eff_props = dict()
    for he in he_list:
        eff_props[he.nom] = ProprieteEffective.objects.filter(nom_he__exact=he.nom)

    # Filtering asked
    filtering = request.GET
    filtered_list = [he.nom for he in he_list]
    if filtering:

        # CI filtering
        filtered_list = remove_ci_from(filtering, filtered_list)

        # Property filtering
        filtered_list = remove_props_from(filtering, filtered_list)

        # Family filtering
        filtered_list = remove_families_from(filtering, filtered_list)

    # context in return
    context = {'he_list': he_list, 'ci_list': ci_list, 'prop_list': prop_list, 'family_list': famille_list,
               'eff_props': eff_props}

    # add filtering context
    if filtering:
        context['filtered_list'] = filtered_list
        if 'contre_indic' in filtering:
            context['contre_indic_filters'] = filtering.getlist('contre_indic')
        if 'property' in filtering:
            context['prop_filters'] = filtering.getlist('property')
        if 'family' in filtering:
            context['family_filters'] = filtering.getlist('family')

    return render(request, 'huiles/index.html', context)


def he_detail(request, he_nom):
    he = get_object_or_404(HuileEssentielle, pk=urllib.unquote(he_nom))
    context = {'huile': he}
    return render(request, 'huiles/huile.html', context)
