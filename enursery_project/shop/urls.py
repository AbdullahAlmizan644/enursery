from django.urls import path
from .views import HomeView,AboutView,ContactView,ShopView,SingleProductView


urlpatterns=[
		path('',HomeView.as_view(), name='home'),
		path('about',AboutView.as_view(),name='about'),
		path('contact',ContactView.as_view(),name="contact"),
		path('shop/<int:pk>/',ShopView.as_view(),name="shop"),
		path('singleProduct/<int:pk>/',SingleProductView.as_view(),name="singleProduct")
]