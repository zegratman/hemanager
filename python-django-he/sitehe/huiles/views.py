# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from models import HuileEssentielle, ContreIndication, ContreIndicationHE, ProprieteEffective, Propriete


# Create your views here.


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
    ci_he_list = None

    # Effective properties
    eff_props = dict()
    for he in he_list:
        eff_props[he.nom] = ProprieteEffective.objects.filter(nom_he__exact=he.nom)

    # Filtering asked
    filtering = request.GET
    filtered_list = [he.nom for he in he_list]
    if filtering:
        if 'contre_indic' in filtering and filtering.get('contre_indic') != 'none':
            excluded_list = ContreIndicationHE.objects.exclude(
                nom_contre_indication__exact=filtering.get('contre_indic'))
            for excluded in excluded_list:
                if excluded.nom_he_id in filtered_list:
                    filtered_list.remove(excluded.nom_he_id)
        if 'property' in filtering and filtering.get('property') != 'none':
            filtered_list = [he for he in filtered_list if
                             len(ProprieteEffective.objects.filter(nom_he__exact=he).filter(
                                 nom_prop__exact=filtering.get('property'))) > 0]

    # context in return
    context = {'he_list': he_list, 'ci_list': ci_list, 'prop_list': prop_list,
               'eff_props': eff_props}

    # add filtering context
    if filtering:
        context['filtered_list'] = filtered_list
        if 'contre_indic' in filtering:
            context['contre_indic_filter'] = filtering.get('contre_indic')
        if 'property' in filtering:
            context['prop_filter'] = filtering.get('property')

    return render(request, 'huiles/index.html', context)


def he_detail(request, he_nom):
    he = get_object_or_404(HuileEssentielle, pk=he_nom)
    context = {'huile': he}
    return render(request, 'huiles/huile.html', context)
