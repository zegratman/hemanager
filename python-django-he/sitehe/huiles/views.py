# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from models import HuileEssentielle, ContreIndication

# Create your views here.


def he_view(request):
    """
    Main view
    :param request: the request
    :return:
    """
    he_list = HuileEssentielle.objects.all()
    ci_list = ContreIndication.objects.all()
    context = {'he_list': he_list, 'ci_list': ci_list}
    return render(request, 'huiles/index.html', context)


def he_detail(request, he_nom):
    he = get_object_or_404(HuileEssentielle, pk=he_nom)
    context = {'huile': he}
    return render(request, 'huiles/huile.html', context)

