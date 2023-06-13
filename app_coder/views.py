from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import *
from django.template import loader
from app_coder.forms import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):

    return render( request , "inicio.html")
    
def contacto(request):

    return render( request , "contacto.html" )



def alumnos(request):
    alumno = Alumno.objects.all()
    return render( request , "alumnos.html",{"alumno":alumno})
 

def alta_alumno(request):
    if request.method == "POST":
        mi_formularioA = Alumno_formulario( request.POST )

        if mi_formularioA.is_valid():
            datos = mi_formularioA.cleaned_data        
            alumno = Alumno( nombre=datos['nombre'] , apellido=datos['apellido'])
            alumno.save()
            alumno = Alumno.objects.all()
            return render( request , "alumnos.html", {"alumno": alumno})
    return render( request, "formularioAlumnos.html")


@login_required
def editar_alumno( request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.apellido = datos['apellido']
            alumno.save()

            alumno = Alumno.objects.all()          
            return render(request , "alumnos.html" , {"alumno": alumno})
    else:
        mi_formulario = Alumno_formulario(initial={'nombre':alumno.nombre , "apellido":alumno.apellido})
    
    return render( request , "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumno": alumno})


@login_required
def elimina_alumno( request , id):

    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()

    return render(request , "alumnos.html" , {"alumno": alumno})







def profesores(request):
    profe= Profesor.objects.all()
    dato = {"profe":profe}
    return render( request , "profesores.html",dato)   


@login_required
def alta_profe(request):

    if request.method == "POST":

        mi_formularioP = Profe_formulario( request.POST )

        if mi_formularioP.is_valid():
            datos = mi_formularioP.cleaned_data        
            profe = Profesor( nombre=datos['nombre'] , apellido=datos['apellido'])
            profe.save()
            profe = Profesor.objects.all()
            return render( request , "profesores.html", {"profes": profe})
    return render( request, "formularioProfes.html")

@login_required
def editar_profe( request , id):

    profe = Profesor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Profe_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profe.nombre = datos['nombre']
            profe.apellido = datos['apellido']
            profe.save()

            profe = Profesor.objects.all()          
            return render(request , "profesores.html" , {"profe": profe})
    else:
        mi_formulario = Profe_formulario(initial={'nombre':profe.nombre , "apellido":profe.apellido})
    
    return render( request , "editar_profe.html" , {"mi_formulario":mi_formulario, "profe": profe})


@login_required
def elimina_profe( request , id):

    profe = Profesor.objects.get(id=id)
    profe.delete()

    profe = Profesor.objects.all()

    return render(request , "profesores.html" , {"profe": profe})








def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    return render( request , "cursos.html", dicc)


@login_required
def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()
            curso = Curso.objects.all()
            return render( request , "cursos.html", {"cursos": curso})

    return render( request, "formulario.html")




@login_required
def buscar_curso(request):

    return render( request , "buscar_curso.html")



@login_required
def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")



@login_required
def elimina_curso( request , id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos": curso})



@login_required
def editar_curso( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos.html" , {"cursos": curso})
    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})








def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "padre.html" ,{"url":avatares[0].imagen.url} )
                
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})



def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")




    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})


def about(request):

    return  render(request, "about.html")


def relleno(request):

    return  render(request, "relleno.html")