from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns=[
    
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^products/(\d+)',views.product_func,name ='product'),
    url(r'^cart/(\d+)',views.add_cart,name ='cart'),
    url(r'^display/',views.display_cart,name ='display'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)