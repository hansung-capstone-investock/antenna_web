from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
import json
from kiwipiepy import Kiwi, Option
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.serializers import *


# Create your views here.
@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        account = accountData.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        return Response(account_serializer.data)

    elif request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        userid = request.data['userid']
        userpw = request.data['userpw']

        account = accountData.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        id = account_serializer.data[0]['id']
        password = account_serializer.data[0]['password']

        if (id, password) == (userid, userpw):
            return JsonResponse({"code": "0000", "msg": "로그인 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"code": "1001", "msg": "로그인 실패하셨습니다."}, status=200)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse({"code": "0000", "msg": "회원가입 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"code": "1001", "msg": "회원가입 실패하셨습니다."}, status=200)