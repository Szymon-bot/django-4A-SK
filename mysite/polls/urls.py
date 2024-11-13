from django.urls import path

from . import views

app_name = "polls"
<<<<<<< HEAD

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
=======
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
>>>>>>> 3240e2301eb005813694940b3f5c5b72e1674087
    path("<int:question_id>/vote/", views.vote, name="vote"),
]