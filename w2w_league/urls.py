"""
URL configuration for w2w_league project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from core import views as core_views  # Using core_views to reference core views
from accounts import views as accounts_views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from core import views

# Custom login and logout views to include messages
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Ensure this points to the correct template

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'  # Ensure this points to the correct template

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "You have successfully logged out!")
        return super().dispatch(request, *args, **kwargs)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('register/', accounts_views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    path('submit-result/', core_views.submit_result, name='submit_result'),
    path('standings/', core_views.standings, name='standings'),
    path('accounts/', include('allauth.urls')),
    path('fia/', core_views.fia, name='fia'),
    path('calendar/', core_views.calendar, name='calendar'),
    path('about/', core_views.about, name='about'),
    path('reaction-game/', core_views.reaction_game, name='reaction_game'),
    path('live-stream/', views.live_stream, name='race_live_stream'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
