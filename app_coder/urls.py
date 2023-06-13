from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("pages" , views.inicio , name="inicio"),
    path("", views.inicio , name= "padre"),
    path("about", views.about, name= "about"),
    path("contacto",views.contacto , name="contacto"),
    path("relleno", views.relleno , name= "relleno"),

    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),

    path("contacto" , views.contacto),
    path("buscar" , views.buscar),

    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    
    path("login" , views.login_request , name="Login"),
    path("register" , views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil"),

    path("alta_profe", views.alta_profe, name= "alta_profe"),
    path("editar_profe/<int:id>", views.editar_profe, name="editar_profe"),
    path("elimina_profe/<int:id>", views.elimina_profe, name= "elimina_profe"),

    path("alta_alumno", views.alta_alumno, name= "alta_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("elimina_alumno/<int:id>", views.elimina_alumno, name= "elimina_alumno"),

]
