from django.conf.urls import  url

from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,basename='login')
router.register('feed',views.User)

urlpatterns=[
    url(r'^hello-view/', views.HelloApiView.as_view()),

    url(r'',include(router.urls))

]
