from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect 
from blog.models import Entrada, Categoria, Mensajes, Contacto
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(published = True)
    return render_to_response('Incio.html',
                              {'posts':posts},
                              context)

def curriculum(request):
    context = RequestContext(request)
    return render_to_response('Curriculum.html',
                              context)

def calculadora(request):
    context = RequestContext(request)
    return render_to_response('Calculadora.html',
                              context)

def conversor(request):
    context = RequestContext(request)
    return render_to_response('Conversor.html',
                              context)

def galeria(request):
    context = RequestContext(request)
    return render_to_response('Galeria.html',
                              context)
def cronometro(request):
    context = RequestContext(request)
    return render_to_response('Cronometro.html',
                              context)
def concurso(request):
    context = RequestContext(request)
    return render_to_response('Concurso.html',
                              context)
def contact(request):
    context = RequestContext(request)
    enviado = "No se envio"
    if request.method == 'POST':
        enviado="Entro al post, por lo menos"
        nombre= request.POST['nombre']
        celu= request.POST['celu']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.celu = celu
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        email = EmailMessage(nombre+' te ha enviado un mail, Renzo', 'Numero: '+celu+"\n"+'Mail: '+mail+"\n\n"+mensaje, to=['elrenzoblog@gmail.com'])
        email.send()        
             
    return render_to_response('contact.html', 
                              {'enviado':enviado},
                              context)

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    mensajes = Mensajes.objects.filter(published_in=mi_post,published = True)
    return render_to_response('post.html', 
                              {'post':mi_post,
                              'mensajes':mensajes}, 
                              context)

def save_message(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Mensajes()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.published_in = mi_post
        msje.save()
        mensajes = Mensajes.objects.filter(published_in=mi_post,published = True)
    
    return render_to_response('mensajes.html', 
                              {'mensajes':mensajes},
                              context)