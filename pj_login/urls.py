from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required



from registration import views

# 実はページを表示するだけならこのように1行で書くことが出来ます。


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # login_requiredで囲むとログイン必須のページになります。
    path("", login_required(views.Index_view.as_view()), name="index"),
    # この１行でdjangoでデフォルトで用意している以下がすべて入ります。
    # ・ログイン
    # ・ログアウト
    # ・パスワード変更
    # ・パスワード再発行
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),

]