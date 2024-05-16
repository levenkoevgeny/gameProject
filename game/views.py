from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from .models import Game, Character, Question, Answer, GameResult
from .serializers import AnswerSerializer, QuestionSerializer, GameResultSerializer
from .filters import GameResultFilter
import datetime


# REST
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GameResultViewSet(viewsets.ModelViewSet):
    queryset = GameResult.objects.all()
    serializer_class = GameResultSerializer
    permission_classes = [AllowAny]
    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


def game_list(request):
    g_list = Game.objects.all()
    return render(request, 'game/game_list.html', {'game_list': g_list})


def new_game_start_page(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/new_game_start_page.html', {'game': game})


def characters_page(request, game_id):
    characters = Character.objects.all()
    return render(request, 'game/characters.html', {'characters': characters, 'game_id': game_id})


def game_running(request):
    context = {}
    if 'game' in request.GET:
        game = get_object_or_404(Game, pk=request.GET.get("game"))
        context['game'] = game

        if 'character' in request.GET:
            question = Question.objects.filter(game=game, character_id=request.GET.get("character"),
                                               question_number=1).first()
            if question:
                context['question'] = question
                context['answers'] = Answer.objects.filter(question=question)
            else:
                pass
    request.session['score'] = 0
    return render(request, 'game/game_main_page.html', context)


@api_view(['GET'])
def write_to_session(request):
    for key, value in request.query_params.items():
        request.session[key] = value
    return Response("Ok", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_session(request):
    session_obj = {'user_name': request.session.get('user_name', ''),
                   'score': request.session.get('score', 0)}
    return Response(session_obj, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_next_question_or_gave_over(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    request.session['score'] = request.session['score'] + answer.score
    if answer.next_question:
        serializer = QuestionSerializer(answer.next_question)
        return Response({'is_game_over': False, 'next_question': serializer.data}, status=status.HTTP_200_OK)
    else:
        result = GameResult(game=answer.question.game, last_name=request.session.get('user_name', 'No data'),
                            score=request.session.get('score', 0), date_time_created=datetime.datetime.now())
        result.save()
        return Response({'is_game_over': True}, status=status.HTTP_200_OK)


def game_over(request):
    return render(request, 'game/game_over.html')


@login_required
def game_results(request):
    qs = GameResult.objects.all()
    f = GameResultFilter(request.GET, queryset=qs)
    return render(request, 'admin/results_list.html', {'filter': f})
