from django.urls import path

from . import views


app_name = 'companies'
urlpatterns = [
    path(
        'create/',
        views.CompanyCreateForm.as_view(),
        name='companycreation'
    ),
    path(
        '<int:pk>/delete/',
        views.CompanyDeleteView.as_view(),
        name='delete'
    ),
    path(
        '<int:pk>/',
        views.CompanyDetailView.as_view(),
        name='detail'
    ),
    path(
        '',
        views.CompanyListView.as_view(),
        name='list'
    ),
    path(
        '<int:pk>/update/',
        views.CompanyUpdateView.as_view(),
        name='update'
    ),
]
