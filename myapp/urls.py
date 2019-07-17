from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('success/', views.success, name="success"),
    path('register_success/', views.register_success, name="register_success"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('tables/', views.tables, name="tables"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
