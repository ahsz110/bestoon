# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User, Expense, Income, Token
from datetime import datetime


@csrf_exempt
def submit_expense(request):
    '''user submits an expense'''
    #TODO: any thing...
    print request.POST
    this_token = request.POST.get('token', '')
    this_user = User.objects.filter(token__token=this_token).get() #useri ke dar jadval token, meghdare tokenesh barabar ba this_token ast.
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    '''user submits an income'''
    #TODO: any thing...
    print request.POST
    this_token = request.POST.get('token', '')
    this_user = User.objects.filter(token__token=this_token).get() #useri ke dar jadval token, meghdare tokenesh barabar ba this_token ast.
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)