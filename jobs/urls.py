from django.urls import path

from . import views


app_name = 'jobs'
urlpatterns = [
    path(
        'for/<int:company_id>/create/',
        views.JobCreateForm.as_view(),
        name='jobcreation'
    ),
    path(
        '<int:pk>/delete/',
        views.JobDeleteView.as_view(),
        name='delete'
    ),
    path(
        '<int:pk>/',
        views.JobDetailView.as_view(),
        name='detail'
    ),
    path(
        '<int:pk>/update/',
        views.JobUpdateView.as_view(),
        name='update'
    ),

    # path(
    #     '',
    #     views.JobListView.as_view(),
    #     name='list'
    # ),
]
