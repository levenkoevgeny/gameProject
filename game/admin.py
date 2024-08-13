from django.contrib import admin
from .models import Game, Question, Answer, GameResult

admin.site.register(Game)
admin.site.register(Question)
# admin.site.register(Answer)
admin.site.register(GameResult)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["get_question", "answer_text", "score", "is_game_over", "game_over_description", "get_next_question"]
    list_display_links = ["answer_text"]

    def get_question(self, obj):
        return obj.question

    def get_next_question(self, obj):
        return obj.next_question if obj.next_question else ""

    get_question.short_description = 'Вопрос №'
    # get_author.admin_order_field = 'book__author'


admin.site.register(Answer, AnswerAdmin)