# --- urls.py to all urls---
from django.urls import path
from . import views

urlpatterns=[
    path('',views.Main.as_view(),name='main'),
    path('sign/',views.UserSigninView.as_view(),name='signin'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('page/<int:page_id>/',views.Page.as_view(),name='page'),
]
# ---end----