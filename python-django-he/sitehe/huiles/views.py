# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from models import HuileEssentielle, ContreIndication, ContreIndicationHE

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
    ci_he_list = None

    # Filtering asked
    filtering = request.GET
    if filtering and filtering.has_key('contre_indic'):
        ci_he_list = ContreIndicationHE.objects.filter(nom_contre_indication=filtering.get('contre_indic'))

    context = {'he_list': he_list, 'ci_list': ci_list, 'ci_he_list': ci_he_list}
    return render(request, 'huiles/index.html', context)


def he_detail(request, he_nom):
    he = get_object_or_404(HuileEssentielle, pk=he_nom)
    context = {'huile': he}
    return render(request, 'huiles/huile.html', context)

