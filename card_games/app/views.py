from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# APP

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

def registrar(request):
    return render(request, 'app/registrar.html')

def pokebusca(request):
    return render(request, 'app/pokebusca.html')

def recientes(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/recientes.html',data)



# CRUD
def agregar_producto(request):
    
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El producto ha sido guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'CRUD/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }
    return render(request, 'CRUD/listar.html', data)





def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_producto")    
        data["form"] = formulario
    
    return render(request, 'CRUD/modificar.html',data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_producto")

#registro

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"],)
            login(request, user)
            # messages.success(request," Te has registrado correctamente")
            #redirigir al home
            return redirect(to="home")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html',data)


# PRODUCTOS

def producto1(request):
    return render(request, 'productos/producto1.html')

def producto2(request):
    return render(request, 'productos/producto2.html')

def producto3(request):
    return render(request, 'productos/producto3.html')

def producto4(request):
    return render(request, 'productos/producto4.html')

def producto5(request):
    return render(request, 'productos/producto5.html')

def producto6(request):
    return render(request, 'productos/producto6.html')

def producto7(request):
    return render(request, 'productos/producto7.html')

def producto8(request):
    return render(request, 'productos/producto8.html')





