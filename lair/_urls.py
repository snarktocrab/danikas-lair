from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('macros/', include('macros.urls'))#,
    #path('admin/', admin.site.urls),
]

