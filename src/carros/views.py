from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from .models import Carr

from .forms import CarroForm, LoginForm, RegisterForm

def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password1 = form.cleaned_data.get('password1')
		password2 = form.cleaned_data.get('password2')


		user = User.objects.create_user(username, password)

		user = authenticate(request, username = username, password=password)
		if user != None:
			login(request, user)
			return redirect('/')
		else:
			request.session['invalid_user'] = 1

	return render(request, "new-users.html", {"form": form})

def logout_view(request):
	logout(request)
	return redirect('/login')


def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username = username, password=password)
		if user != None:
			login(request, user)
			return redirect('/')
		else:
			request.session['invalid_user'] = 1

	return render(request, "login.html", {"form": form})

def all_cars(request, *args, **kwargs):
	all_obj = Carr.objects.all()
	return render(request, "all_cars.html", {'my_list': all_obj})

# def login(request):
# 	return render(request, 'login.html', {})

def vender(request):
	#print(request.POST)
	if request.method == 'POST' and request.FILES['upload']:
		print(request.POST)
		upload = request.FILES['upload']
		fss = FileSystemStorage()
		file = fss.save(upload.name, upload)
		file_url = fss.url(file)
		Carr.objects.create(Marca = request.POST.get('Marca'),
							Modelo = request.POST.get('Modelo'),
							Motor = request.POST.get('Motor'),
							Ano = request.POST.get('Ano'),
							Cambio = request.POST.get('Cambio'),
							Combustivel = request.POST.get('Combustivel'),
							Km = request.POST.get('Km'),
							Preco = request.POST.get('Preco'),
							Img_url = file_url)

		return redirect(f"""/carro/{Carr.objects.latest('id').id}""")
	else:
		return render(request, 'vender.html', {})

def new_user(request):
	return render(request, 'new-users.html', {})

def carro_detail_view(request, id):
	obj = get_object_or_404(Carr, id = id)
	context = {
		'Marca': obj.Marca,
		'Modelo': obj.Modelo,
		'Motor': obj.Motor,
		'Ano': obj.Ano,
		'Cambio': obj.Cambio,
		'Combustivel': obj.Combustivel,
		'Km': obj.Km,
		'Img_url': obj.Img_url
	}
	return render(request, "carro_detail_view.html", context)
