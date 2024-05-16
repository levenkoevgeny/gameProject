from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from game import views as game_views

from rest_framework import routers
router = routers.DefaultRouter()


router.register(r'answers', game_views.AnswerViewSet)
router.register(r'questions', game_views.QuestionViewSet)
router.register(r'results', game_views.GameResultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/game")),
    path('game/', include('game.urls')),
    path('api/', include(router.urls)),
    path('api/write-to-session', game_views.write_to_session),
    path('api/get_user_session', game_views.get_user_session),
    path('api/get_next_question/<int:pk>/', game_views.get_next_question_or_gave_over),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)