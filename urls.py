from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name='model_form_upload'),
    url(r'^a$',views.editar,name='editar'),
    url(r'^student$', views.student,name='student'),
]

