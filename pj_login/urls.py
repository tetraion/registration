from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required



from registration import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # login_requiredでログイン必須のページ
    path("", login_required(views.Index_view.as_view()), name="index"),
    # djangoデフォルトログイン
    # ・ログイン
    # ・ログアウト
    # ・パスワード変更
    # ・パスワード再発行
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),

]
