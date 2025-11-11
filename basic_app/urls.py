
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('web/',views.web,name='web'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('audio/',views.audio,name='audio'),
    path('wearables/',views.wearables,name='wearables'),
    path('drones/',views.drones,name='drones'),
    path('accessories/',views.accessories,name='accessories'),
    path('watches/',views.watches,name='watches'),
    path('bags/',views.bags,name='bags'),
    path('eyewear/',views.eyewear,name='eyewear'),
    path('all_products/',views.all_products,name='all_products'),
    path('head_p/',views.head_p,name='head_p'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/',views.shop,name='shop'),
    path('card_page/',views.card_page,name='card_page'),
    path('description/',views.description,name='description')
]
