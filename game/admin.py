from django.contrib import admin
from .models import Game, Question, Answer, GameResult, Character

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GameResult)
admin.site.register(Character)
