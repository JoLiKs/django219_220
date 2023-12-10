import asyncio

from django import forms

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from bot import main
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

from .forms import UserForm
from .models import Image, ModelAnna


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']



@csrf_exempt
def reg(request):
    anna = ModelAnna()
    if request.method == 'POST':
        data = ModelAnna.objects.all()
        for i in data:
            if request.POST['email'] == i.email: return render(request, 'anna.html', {"err": "Данный Email занят"})
        if len(request.POST['password']) < 6: return render(request, 'anna.html', {"err": "Пароль слишком короткий"})
        anna.pole = 'Hello world'
        anna.email = request.POST['email']
        anna.password = request.POST['password']
        anna.save()
        return HttpResponse('Email'+' '+anna.email+' '+"успешно зарегистрирован!")

    return render(request, 'reg.html', {"err": ""})

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.body)
        print('Bot started!')
        asyncio.run(main())

    else:
        img = ImageForm()
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # engine = create_engine('sqlite:///db.sqlite3')
        # Base = declarative_base()
        # Session = sessionmaker(bind=engine)
        # session = Session()
        # session.execute(text("""select * from project_modelanna"""))
        # data = session.flush()
        # session.close()
        data = ModelAnna.objects.all()
        for i in data:
            if email == i.email:
                if password == i.password:
                    return HttpResponse("Вы успешно прошли авторизацию!")
                else:
                    return HttpResponse("Пароль неверный")
        return HttpResponse("Такого пользователя не существует")
    return render(request, 'login.html')


@csrf_exempt
def mails(request):
    if request.method == 'POST':
        pass
    render(request, 'index.html')
    return render(request, 'danger.html')

