from django.db import models


class Game(models.Model):
    game_title = models.TextField(verbose_name='Название игры')
    game_description = models.TextField(verbose_name='Описание игры', blank=True, null=True)
    task_text = models.TextField(verbose_name='Текст задания', blank=True, null=True)
    task_img = models.ImageField(verbose_name='Картинка к игре', blank=True, null=True, upload_to='media/games')

    def __str__(self):
        return self.game_title

    class Meta:
        ordering = ('id',)
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Character(models.Model):
    character_name = models.CharField(verbose_name='Имя персонажа', max_length=100)
    character_img = models.ImageField(verbose_name='Аватар', blank=True, null=True, upload_to='media/characters')
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return self.character_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Question(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, verbose_name="Персонаж", blank=True, null=True)
    is_first_question_in_game = models.BooleanField(verbose_name="Является первым вопросом в игре", default=False)
    question_text = models.TextField(verbose_name='Текст вопроса')
    question_number = models.CharField(max_length=20, verbose_name='Порядковый номер')
    question_img = models.ImageField(verbose_name='Картинка к вопросу', blank=True, null=True, upload_to='media/questions')
    question_img_description = models.TextField(verbose_name='Текст к картинке', blank=True, null=True)

    def __str__(self):
        return self.question_number + ' ' + self.question_text

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', related_name='answers')
    answer_text = models.TextField(verbose_name='Текст ответа')
    score = models.IntegerField(verbose_name='Баллы за ответ')
    next_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Следующий вопрос', related_name='next_question' ,blank=True, null=True)
    is_game_over = models.BooleanField(verbose_name='Игра проиграна', default=False)
    game_over_description = models.TextField(verbose_name='Описание причины проигрыша', blank=True, null=True)
    is_last_answer_in_game = models.BooleanField(verbose_name='Является последним в игре', default=False)

    def __str__(self):
        return self.answer_text + ' ' + self.question.question_number

    class Meta:
        ordering = ('id',)
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class GameResult(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра", related_name='results')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    date_time_created = models.DateTimeField(auto_created=True, verbose_name="Дата и время создания записи")
    score = models.IntegerField(verbose_name="score")

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Результат игры'
        verbose_name_plural = 'Результаты игры'
