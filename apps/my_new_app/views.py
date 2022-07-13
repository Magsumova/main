from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import QuerySet
from typing import Any
from .models import Account, Student



# def index(request: WSGIRequest) ->HttpResponse:
#     user: User = User.objects.first()
#     account: Account = Account.objects.get(user = user)
#     student: Student = Student.objects.first()
#     name: str = account.full_name
#     gpa: int = student.gpa
#     firstname: str = user.first_name
    
#     text = f'<h1>{name}</h1>\
#             <h1>{gpa}</h1>\
#             <h1>{firstname}</h1>'
#     response: HttpResponse = HttpResponse(text)
    
#     return response

def index(request: WSGIRequest) ->HttpResponse:
    users: QuerySet = User.objects.all()
    context = {
        'title': 'Main Page',
        'users': users
    }
    
    return render(request, 'index.html', context)

def admin(request: WSGIRequest) ->HttpResponse:
    return render(
        request, 
        'admin.html',
        context={"users":User.objects.all()} 
    )

def show(request: WSGIRequest) ->HttpResponse:
    return render(
        request,
        'show.html'
    )