"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, addToCart, contact, shop, shopingcart, remove_from_url, order, order_data, thanks, signup, signin, signout, sendContact, sendContacts
from django.conf.urls.static import static
from my_project.settings import MEDIA_URL, MEDIA_ROOT
urlpatterns = [
    path('', index, name='index'),
    path('addToCart/<int:id>', addToCart, name='addToCart'),
    path('shop', shop, name='shop'),
    path('shopingcart', shopingcart, name='shopingcart'),
    path('remove_from_url/<int:pk>', remove_from_url, name='remove_from_url'),
    path('order/', order, name='order'),
    path('order_data/', order_data, name='order_data'),
    path('thanks/', thanks, name='thanks'),
    path('signup', signup, name='signup'),    # регистрация 
    path('signin', signin, name='signin'),    # войти
    path('signout', signout, name='signout'), # выход
    path('contact', contact, name='contact'),
    path('sendContact/', sendContact, name='sendContact'),
    path('sendContacts/', sendContacts, name='sendContacts'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)