from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views


urlpatterns = [
    path('',views.Home,name='home'),
    path('health/',views.health,name='health'),
    path('signup/', views.signup, name="signup"),  
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
    path('contact/',views.contact,name='contact'),
    path('appointment/',views.Appointmentfun,name='appointment'),
    path('login/',views.loginfun,name='login'),
    path('logout',views.logoutfun,name='logout'),
    path('password_reset/',views.PaswordresetviewFun.as_view(),name='password_reset'),
    path('password_reset/done/',views.PasswordResetdoneviewFun.as_view(),name='password_reset_done'),
    path("password-reset-confirm/<uidb64>/<token>/",views.PasswordREsetConformViewFun.as_view(),name='password_reset_confirm'),
    path("password-reset-complete/",views.PasswordResetCompleteVIewFun.as_view(), name="password_reset_complete"),
    path('appdetail',views.AppointmentDetail,name='appd')



   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

