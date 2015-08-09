from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^curriculum/', 'blog.views.curriculum', name='curriculum'),
                       url(r'^calculadora/', 'blog.views.calculadora', name='calculadora'),
                       url(r'^conversor/', 'blog.views.conversor', name='conversor'),
                       url(r'^galeria/', 'blog.views.galeria', name='galeria'),
                       url(r'^cronometro/', 'blog.views.cronometro', name='cronometro'),    
                       url(r'^concurso/', 'blog.views.concurso', name='concurso'),
                       url(r'^contactame/', 'blog.views.contact', name='contactame'),                       
                       url(r'^save_message/$', 'blog.views.save_message', name='save_message')
                        )