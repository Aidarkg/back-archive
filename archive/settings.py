from pathlib import Path
from decouple import config
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'data_media',
    'moderator',
    'faq',
]

REST_FRAMEWORK = {
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
    
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'archive.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'archive.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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



LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# подключил редис
REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')

# подключил селери
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'


JAZZMIN_SETTINGS = {
    # Название окна (по умолчанию будет использоваться current_admin_site.site_title, если отсутствует или None)
    "site_title": "Администрирование библиотеки",

    # Заголовок на экране входа (максимум 19 символов) (по умолчанию будет использоваться current_admin_site.site_header, если отсутствует или None)
    "site_header": "Администрация архива президента",

    # Заголовок бренда (максимум 19 символов) (по умолчанию будет использоваться current_admin_site.site_header, если отсутствует или None)
    "site_brand": "Архив президента",

    # Логотип для вашего сайта, должен быть доступен в статических файлах, используется для бренда в верхнем левом углу
    "site_logo": "site_logo.png",

    # Логотип для формы входа, должен быть доступен в статических файлах (по умолчанию используется site_logo)
    "login_logo": None,

    # Логотип для формы входа в темных темах (по умолчанию используется login_logo)
    "login_logo_dark": None,

    # CSS-классы, применяемые к логотипу выше
    "site_logo_classes": "img-circle",

    # Относительный путь к favicon для вашего сайта, будет использоваться по умолчанию site_logo, если отсутствует (идеально 32x32 пикселя)
    "site_icon": None,

    # Приветственный текст на экране входа
    "welcome_sign": "Добро пожаловать в библиотеку",

    # Авторское право в подвале
    "copyright": "Acme Library Ltd",

    # Список администраторов модели для поиска из строки поиска, строка поиска опущена, если исключена
    # Если вы хотите использовать одно поле поиска, вам не нужно использовать список, вы можете использовать простую строку
    "search_model": ["auth.User", "auth.Group"],

    # Имя поля в модели пользователя, которое содержит поле изображения/URL/Charfield или функцию обратного вызова, которая получает пользователя
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Ссылки для размещения в верхнем меню
    "topmenu_links": [

        # URL, который будет развернут (Разрешения могут быть добавлены)
        {"name": "Главная",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # Внешний URL, который открывается в новом окне (Разрешения могут быть добавлены)
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # модель администратора, на которую будет ссылка (Проверяются разрешения для модели)
        {"model": "auth.User"},

        # Приложение с выпадающим меню на все его страницы моделей (Проверяются разрешения для моделей)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Дополнительные ссылки для включения в меню пользователя в верхнем правом углу (тип url "app" не разрешен)
    "usermenu_links": [
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Показывать ли боковое меню
    "show_sidebar": True,

    # Раскрыть ли меню автоматически
    "navigation_expanded": True,

    # Скрыть эти приложения при создании бокового меню, например (auth)
    "hide_apps": [],

    # Скрыть эти модели при создании бокового меню (например, auth.user)
    "hide_models": [],

    # Список приложений (и/или моделей) для определения порядка бокового меню (не обязательно включать все приложения/модели)
    "order_with_respect_to": ['moderator', 
                              'data_media', 'data_media.VideoData', 'data_media.PhotoGallery', 
                              'faq'],

    # Пользовательские ссылки для добавления в группы приложений, сгруппированные по имени приложения
    "custom_links": {
        "books": [{
            "name": "Создать сообщение", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Пользовательские значки для приложений/моделей бокового меню
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    # Значки, которые используются, когда не указаны вручную
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Использовать модальные окна вместо всплывающих окон
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Относительные пути к пользовательским CSS/JS скриптам (должны присутствовать в статических файлах)
    "custom_css": None,
    "custom_js": None,
    # Указываете ли шрифт из fonts.googleapis.com (используйте custom_css для предоставления шрифта в противном случае)
    "use_google_fonts_cdn": True,
    # Показывать ли пользовательский интерфейс настройки в боковой панели
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Отображать вид изменений как одна форма или вкладки, текущие варианты
    # - single
    # - horizontal_tabs (по умолчанию)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # переопределение форм изменений на основе модели администратора
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Добавить выпадающий список языков в административную панель
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}