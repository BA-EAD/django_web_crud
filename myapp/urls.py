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
    path('edit_profile/<int:id>', views.edit_profile, name="edit_profile"),
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('show_profile/<int:id>', views.show_profile, name="show_profile"),
    path('email/', views.email, name="email"),
    path('confirm_password/', views.confirm_password, name="confirm_password"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
