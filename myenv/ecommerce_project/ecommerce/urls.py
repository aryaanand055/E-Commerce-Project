from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('products/<int:product_id>', views.product_detail, name='product_detail'),
    path('products/<str:category>', views.productCategory, name='product_category'),
    path('cart/', views.cart, name='cart'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)