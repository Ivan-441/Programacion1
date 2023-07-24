from django.shortcuts import render, redirect
from .models import Cliente, Actividad, Pago, Inscripcion
from django.contrib.auth.decorators import login_required

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "gestionClientes.html", {"clientes": clientes})

@login_required
def actividades(request):
    actividades = Actividad.objects.all()
    return render(request, "gestionActividades.html", {"actividades": actividades})

@login_required
def registrarActividad(request):
    nombre = request.POST['nombre']
    codigo = request.POST['codigo']
    Actividad.objects.create(nombre=nombre, codigo=codigo)
    return redirect('/actividades')

@login_required
def eliminarActividad(request, codigo):
    actividad = Actividad.objects.get(codigo=codigo)
    actividad.delete()
    return redirect('/actividades')


@login_required
def pagos(request):
    pagos = Pago.objects.all()
    clientes = Cliente.objects.all()
    return render(request, "gestionPagos.html", {"pagos": pagos, "clientes":clientes})

@login_required
def registrarPago(request):
    monto = request.POST['monto']
    dni_cliente = request.POST['dni']
    cliente = Cliente.objects.get(dni=dni_cliente)

    Pago.objects.create(monto=monto, dni_cliente=cliente)
    return redirect('/pagos')

@login_required
def inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    actividades = Actividad.objects.all()
    clientes = Cliente.objects.all()
    return render(request, "gestionInscripciones.html", {"inscripciones": inscripciones, "actividades": actividades, "clientes": clientes})

@login_required
def eliminarInscripcion(request, actividad, dni_cliente):
    inscripcion = Inscripcion.objects.get(actividad=actividad, dni_cliente=dni_cliente)
    inscripcion.delete()
    return redirect('/inscripciones')

@login_required
def registrarInscripcion(request):
    codigo = request.POST['actividad']
    dni_cliente = request.POST['dni']

    actividad = Actividad.objects.get(codigo=codigo)
    dni = Cliente.objects.get(dni=dni_cliente)

    Inscripcion.objects.create(actividad=actividad, dni_cliente=dni)
    return redirect('/inscripciones')

@login_required
def registrarCliente(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    dni = request.POST['dni']
    email = request.POST['email']
    fecha_nacimiento = request.POST['fecha_nacimiento']

    Cliente.objects.create(nombre=nombre, apellido=apellido, dni=dni, email=email, fecha_nacimiento=fecha_nacimiento)
    return redirect('/')

@login_required
def eliminarCliente(request, dni):
    cliente = Cliente.objects.get(dni=dni)
    cliente.delete()
    return redirect('/')

@login_required
def edicionCliente(request, dni):
    cliente = Cliente.objects.get(dni=dni)
    return render(request, "edicionCliente.html", {"cliente": cliente})

@login_required
def editarCliente(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    dni = request.POST['dni']
    fecha_nacimiento = request.POST['fecha_nacimiento']

    cliente = Cliente.objects.get(dni=dni)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.email = email
    cliente.fecha_nacimiento = fecha_nacimiento
    
    cliente.save()

    return redirect('/')

@login_required
def eliminarPago(request, id):
    pago = Pago.objects.get(id=id)
    pago.delete()
    return redirect('/pagos')