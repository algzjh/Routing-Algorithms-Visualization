"""RouteVisProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin  # 导入 Admin 功能模块
from django.urls import include, path  # 导入 URL 编写模块

# urlpatterns 整个项目的 url 集合，每个元素代表一条 url 信息
# RouteVisApp1.urls 是 url 的处理函数，也称为视图函数
urlpatterns = [
    path('RouteVisApp1/', include('RouteVisApp1.urls')),
    path('admin/', admin.site.urls),
]
