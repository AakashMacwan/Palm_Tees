from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<product_id>/', views.productdetail, name='details'),
    path('cart', views.cart, name='cart'),
    path('cart/delete/', views.removeitem, name='removeitem')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 