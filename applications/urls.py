from django.urls import path

from . import views


app_name = 'applications'
urlpatterns = [
    path(
        '<int:job_id>/apply/',
        views.ApplicationCreateForm.as_view(),
        name='applicationform'
    ),
    path(
        '<int:pk>/detail/',
        views.ApplicationDetailView.as_view(),
        name='detail'
    ),
    path(
        'thankyou/',
        views.thankyou,
        name='thankyou'
    ),
]
