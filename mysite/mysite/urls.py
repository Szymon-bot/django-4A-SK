from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

app_name = "polls"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls"))
]
=======
from django.urls import include, path

urlpatterns = [
	path("polls/", include("polls.urls")),
	path("admin/", admin.site.urls),
]
>>>>>>> 3240e2301eb005813694940b3f5c5b72e1674087
