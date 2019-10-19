"""
Django settings for RouteVisProject project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
"""
常用的 Web 应用程序
会话控制：Session 存储在服务器端，Cookie 存储在客户端
Django 提供 5 种不同的缓存方式：Memcached、全站缓存、视图缓存、路由（URL）缓存、模板缓存
CSRF 防护只作用于 POST 请求，并不防护 GET 请求，因为 GET 请求以只读形式访问网站资源，
并不破坏和篡改网站数据。
如果网页某些数据是使用前端的 Ajax 实现表单提交的，那么 Ajax 向服务器发送 POST 请求时，
请求参数必须添加 csrftoken 的信息，否则服务器会视该请求是恶意请求。
Django 的分页功能由模块 Paginator 实现，开发者可以调用模块所提供的函数实现网站的分页功能
"""
"""
Django 项目线上部署
Nginx+uWSGI+Django
Nginx 作为服务器最前端，负责接收浏览器的所有请求并统一管理。
静态请求由 Nginx 自己处理，非静态请求通过 uWSGI 服务器传递给 Django 应用，
由 Django 进行处理并做出相应，从而完成一次 Web 请求。
"""
"""
网站 API 也称为接口，接口其实与网站的 URL 地址是同一个原理。
当用户使用 GET 或者 POST 方式访问接口时，接口以 JSON 或字符串的数据内容返回给用户，
网站的 URL 地址主要返回的是 HTML 网页信息。
可以使用 Django Rest Framework 框架实现
验证码：django-simple-captcha
站内搜索引擎：django-haystack
第三方注册：django-social-auth
分布式：Celery 框架，是 Python 开发的分布式任务队列，
使用第三方消息服务来传递任务，目前支持 RabbitMQ，Redis，MongoDB 等。
eventlet：Python 的协程并发库
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目路径：通过os模块读取当前项目在系统的具体路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥配置：用于重要数据的加密处理，如用户密码，CSRF机制，会话Session等
# 用户密码：内置的用户管理系统
# CSRF：Cross-site request forgery，跨站请求伪造，主要用于表单提交
# 会话Session：Session的信息存放在Cookies，标识当前访问网站的用户身份
SECRET_KEY = 'dy3=pddd-q9z5ndsqmn9j2xn!25+5ya8e+d&frx=hbz*9c@*q1'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式：如果设为True，会自动检测代码是否发生更改，根据检测结果执行是否刷新重启系统
DEBUG = True

# 域名访问权限
# 当DEBUG为True并且ALLOWED_HOSTS为空时，只允许localhost或127.0.0.1在浏览器上访问
# 当DEBUG为False时，ALLOWED_HOSTS为必填项，ALLOWED_HOSTS=[*]允许所有域名访问
ALLOWED_HOSTS = []


# Application definition
# App列表：告诉Django有哪些App
INSTALLED_APPS = [
    'RouteVisApp1.apps.Routevisapp1Config',
    'django.contrib.admin',  # 内置的后台管理系统
    'django.contrib.auth',  # 内置的用户认证系统
    'django.contrib.contenttypes',  # 记录项目中所有的model元数据（Django的ORM框架）
    'django.contrib.sessions',  # Session会话功能，用于标识当前访问网站的用户身份，记录相关用户信息
    'django.contrib.messages',  # 消息提示功能，如填完表单或完成输入后，网站会有相关的操作提示
    'django.contrib.staticfiles',  # 查找静态资源路径
]

# 中间件是处理Django的request和response对象的钩子
# Django首先经过中间件处理用户请求信息，执行相关的处理，然后将结果返回给用户
# 设置顺序是固定的
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # 内置的安全机制
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话 Session 功能
    'django.middleware.common.CommonMiddleware',  # 处理请求信息，规范化请求内容
    'django.middleware.csrf.CsrfViewMiddleware',  # 开启 CSRF 防护功能
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 开启内置的用户认证系统
    'django.contrib.messages.middleware.MessageMiddleware',  # 开启内置的信息提示功能
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止恶意程序点击劫持
]

ROOT_URLCONF = 'RouteVisProject.urls'

# 设置模板路径是告诉Django在解析模板时，如何找到模板所在的位置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # BACKEND：定义模板引擎，内置的有DjangoTemplates和jinja2
        'DIRS': [],  # 设置模板所在路径，默认为空列表
        # [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'index/templates')]
        'APP_DIRS': True,  # 是否在App里查找模板文件
        'OPTIONS': {  # 用于填充在RequestContext中上下文的调用函数，一般情况下不做修改
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'RouteVisProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Django提供4种数据库引擎：postgresql, mysql, sqlite3, oracle
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# STATIC_URL是必须配置的属性，只能识别App里的static静态资源文件夹
# STATICFILES_DIRS是可选配置属性，为列表或元组格式，每个元素代表一个静态资源文件夹
STATIC_URL = '/static/'
