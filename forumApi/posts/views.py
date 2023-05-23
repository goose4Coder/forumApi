from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


def main_page(request):
    return HttpResponse('It is the main page!')


def get_user_info(request):
    return JsonResponse({'name':request.user.username, 'id':request.user.id})