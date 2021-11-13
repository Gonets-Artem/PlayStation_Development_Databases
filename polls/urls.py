from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls')),
    path('designer/', views.get_designer),
    path('design/', views.get_design),
    path('dualshock/', views.get_dualshock),
    path('ps_vr/', views.get_ps_vr),
    path('developer/', views.get_developer),
    path('software/', views.get_software),
    path('form_factor/', views.get_form_factor),
    path('prototype/', views.get_prototype),
    path('console/', views.get_console),
    path('advertising_department/', views.get_advertising_department),
    path('feedback/', views.get_feedback),
    path('target_audience/', views.get_target_audience),
    path('pr_manager/', views.get_pr_manager),
    path('competitor/', views.get_competitor),
    path('market_analysis/', views.get_market_analysis),
    path('product_manager/', views.get_product_manager),
    path('plant/', views.get_plant),
    path('storage_room/', views.get_storage_room),
    path('component/', views.get_component),
    path('supplier/', views.get_supplier),
    path('equipment/', views.get_equipment),
    path('equipment_condition/', views.get_equipment_condition),
    path('employee/', views.get_employee),
    path('kit/', views.get_kit)
]
