from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Alumno,Genero

from .forms import GeneroForm



# Create your views here.
def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,'alumnos/index.html', context)

def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_Add.html', context)
    
    else:


        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["aPaterno"]
        aMaterno=request.POST["aMaterno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        if "activo" in request.POST:
            activo=1
        else:
            activo=0

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=activo)
        obj.save()
        context={'mensaje': "Ok, Datos Ingresados Correctamente..."}
        return render(request, 'alumnos/alumnos_add.html', context)
    


def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, Datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.htmt', context)
    except:
        mensaje = "Error, Rut no existe..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)


def alumnos_findEdit(request,pk):

    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        generos= Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno, 'generos':generos}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context={'mensaje':"Error, Rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)
        


def alumnosUpdate(request):
    if request.method == "POST":


        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje': "Ok, datos actualizados...",'generos':generos,'alumno':alumno}
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:

        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)
    


def crud_generos(request):
    generos = Genero.objects.all()
    context = {'generos':generos}
    print("Enviando datos generos_list")
    return render(request,"alumnos/generos_list.html", context)

def generosAdd(request):
    print("estoy en el controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un POST...")
        form= GeneroForm(request.POST)
        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=GeneroForm()

            context={'mensaje':"Ok, Datos grabados...","form":form}
            return render(request,"alumnos/generos_add.html", context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'alumnos/generos_add.html', context)
    

def generos_del(request,pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, Datos eliminados...")
            context = {'generos': generos, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'alumnos/generos_list.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje': mensaje, 'generos':generos}
        return render(request, 'alumnos/generos_list.html', context)
    

def generos_edit(request,pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontro el genero...")
            if request.method == "POST":
                print("Edit, es un post")
                form = GeneroForm(request.POST,instance=genero)
                form.save()
                mensaje="Bien, Datos actualizados..."
                print("Mensaje")
                context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'alumnos/generos_edit.html', context)
            else:
                #no es un POST
                print("Edit, No es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context={'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'alumnos/generos_edit.html', context)
    except:
        print("Error, Id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, Id no existe"
        context={'mensaje': mensaje, 'generos':generos}
        return render(request, 'alumnos/generos_edit.html', context)
    
def menu(request):
    request.session["usuario"]="Alan"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'alumnos/menu.html', context)





        

