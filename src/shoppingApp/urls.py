from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product, name='product'),
    path('cart/<str:id>', views.cart, name='cart'),
    path('offerApply/<str:id>', views.offerApply, name='offerApply'),
	path('thankyou/', views.thankyou, name='thankyou'),
    path('checkout/payment/<str:id>', views.payment, name='payment'),
    path('product/addproduct', views.addproduct, name='addproduct'),
    # path('addToCart/<list_id>', views.addToCart, name='addToCart'),
    path('addToCart/<str:id1>/<str:id2>/', views.addToCart, name='addToCart'),
    path('deleteToCart/<list_id>', views.deleteToCart, name='deleteToCart'),
    # path('product/create',views.productCreateView.as_view(), name="create"),
]
