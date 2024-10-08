# Generated by Django 5.0.4 on 2024-08-13 06:13
from django.db import migrations

from game.models import Game, Question, Answer


def init_questions(apps, schema_editor):
    Game.objects.all().delete()
    Question.objects.all().delete()
    Answer.objects.all().delete()
    game = Game.objects.create(game_title='Игра 1')
    Question.objects.create(game=game,
                            question_text="Вы сотрудник НЦБ Интерпола в Республике Беларусь и получаете посредством информационной системы I-24/7 розыскной циркуляр "
                                          "с красным углом о том, что по адресу: г. Минск, ул. Интернациональная, 14-5, проживает находящийся в международном розыске "
                                          "гражданин Австрии Штайер А. (инициатор розыска – Дания). Ваши действия?",
                            is_first_question_in_game=True,
                            question_number=1)

    Question.objects.create(game=game,
                            question_text="Вы проверяете является ли совершенное действие противоправным в соответствии с УК Республики Беларусь",
                            question_number=2)

    Question.objects.create(game=game,
                            question_text="Совершенные лицом действия являются тяжким преступлением",
                            question_number=3)

    Question.objects.create(game=game,
                            question_text="Совершенные лицом действия являются менее тяжким преступлением",
                            question_number=4)

    Question.objects.create(game=game,
                            question_text="Вы сотрудник НЦБ Интерпола в Республике Беларусь и получаете посредством информационной системы I-24/7 розыскной циркуляр "
                                          "с красным углом о том, что по адресу: г. Минск, ул. Интернациональная, 14-5, проживает находящийся в международном розыске "
                                          "гражданин Австрии Штайер А. (инициатор розыска – Дания). Ваши действия?",
                            question_number=5)

    Question.objects.create(game=game,
                            question_text="Поступление карточки регистрации события/правонарушения/ преступления в ОДС ОВД. Действия оперативного дежурного",
                            question_number=6)

    Question.objects.create(game=game,
                            question_text="Сотрудники ОВД выбыли по адресу проживания разыскиваемого и задержали его. Действия сотрудников:",
                            question_number=7)

    Question.objects.create(game=game,
                            question_text="Сотрудники ОВД задержали разыскиваемого в порядке ст. 510 УПК Республики Беларусь. "
                                          "После составления протокола задержания и личного обыска они осуществляют (указать действия и их порядок):",
                            question_number=8)

    Question.objects.create(game=game,
                            question_text="Прокурор, опросив лицо, находящееся в международном розыске с целью выдачи, может принять решение:",
                            question_number=9)

    Question.objects.create(game=game,
                            question_text="Прокурор применяет к лицу, находящемуся в международном розыске с целью выдачи, "
                                          "меру пресечения в виде заключения под стражу сроком:",
                            question_number=10)

    Question.objects.create(game=game,
                            question_text="А также совершает следующие действия:",
                            question_number=11)

    Question.objects.create(game=game,
                            question_text="Вариант развития событий: Сотрудники ОВД не обнаружили разыскиваемого по указанному адресу:",
                            question_number=12)

    Question.objects.create(game=game,
                            question_text="Необходимо ли сотрудникам ОВД письменно уведомлять НЦБ Интерпола в "
                                          "Республике Беларусь о проведенных мероприятиях:",
                            question_number=13)

    Question.objects.create(game=game,
                            question_text="Уведомляет ли НЦБ Интерпола в Республике Беларусь государство-инициатора "
                                          "розыска лица о проведенных мероприятиях и их результатах:",
                            question_number=14)

    # Answers

    Answer.objects.create(question=Question.objects.get(question_number=1),
                          answer_text="Вы проверяете является ли совершенное действие противоправным в соответствии с УК Республики Беларусь)",
                          score=2,
                          next_question=Question.objects.get(question_number=2))
    Answer.objects.create(question=Question.objects.get(question_number=1),
                          answer_text="Вы выезжаете для задержания лица сами вместе с коллегой из НЦБ Интерпола в Республике Беларусь",
                          score=1,
                          next_question=Question.objects.get(question_number=7))
    Answer.objects.create(question=Question.objects.get(question_number=1),
                          answer_text="Вы направляете уведомление в РУВД/РОВД по месту регистрации и проживания разыскиваемого лица",
                          score=2,
                          next_question=Question.objects.get(question_number=6))

    Answer.objects.create(question=Question.objects.get(question_number=2),
                          answer_text="Совершенные лицом действия в Республике Беларусь являются тяжким преступлением",
                          score=0,
                          next_question=Question.objects.get(question_number=3))
    Answer.objects.create(question=Question.objects.get(question_number=2),
                          answer_text="Совершенные лицом действия в Республике Беларусь являются менее тяжким преступлением",
                          score=0,
                          next_question=Question.objects.get(question_number=4))

    Answer.objects.create(question=Question.objects.get(question_number=3),
                          answer_text="необходимо осуществить задержание",
                          score=1,
                          next_question=Question.objects.get(question_number=5))
    Answer.objects.create(question=Question.objects.get(question_number=3),
                          answer_text="не осуществлять задержание лица, разыскиваемого другим государством",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=4),
                          answer_text="необходимо осуществить задержание",
                          score=1,
                          next_question=Question.objects.get(question_number=5))
    Answer.objects.create(question=Question.objects.get(question_number=4),
                          answer_text="не осуществлять задержание лица, разыскиваемого другим государством",
                          score=-1)

    Answer.objects.create(question=Question.objects.get(question_number=5),
                          answer_text="Вы выезжаете для задержания лица сами вместе с коллегой из НЦБ Интерпола в Республике Беларусь",
                          score=1,
                          next_question=Question.objects.get(question_number=7))
    Answer.objects.create(question=Question.objects.get(question_number=5),
                          answer_text="Вы направляете уведомление в РУВД/РОВД по месту регистрации и проживания разыскиваемого лица",
                          score=2,
                          next_question=Question.objects.get(question_number=6))

    Answer.objects.create(question=Question.objects.get(question_number=6),
                          answer_text="НАПРАВЛЯЕТ Сотрудников ОВД для задержания лица",
                          score=1,
                          next_question=Question.objects.get(question_number=7))
    Answer.objects.create(question=Question.objects.get(question_number=6),
                          answer_text="НЕ РЕАГИРОВАТЬ не регистрировать / не создавать материал проверки сообщения",
                          score=-2)

    Answer.objects.create(question=Question.objects.get(question_number=7),
                          answer_text="ЗАДЕРЖАНИЕ в порядке ст. 510 УПК Республики Беларусь",
                          score=1,
                          next_question=Question.objects.get(question_number=8))
    Answer.objects.create(question=Question.objects.get(question_number=7),
                          answer_text="ЗАДЕРЖАНИЕ в порядке ст. 108 УПК Республики Беларусь",
                          score=-1)

    Answer.objects.create(question=Question.objects.get(question_number=8),
                          answer_text="Вынесение постановления о задержании",
                          score=1)
    Answer.objects.create(question=Question.objects.get(question_number=8),
                          answer_text="Передачу задержанного следователю РО СК",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=8),
                          answer_text="Опрос лица",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=8),
                          answer_text="Передачу задержанного прокурору района",
                          score=1,
                          next_question=Question.objects.get(question_number=9))

    Answer.objects.create(question=Question.objects.get(question_number=9),
                          answer_text="Об освобождении",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=9),
                          answer_text="О заключении под стражу",
                          score=1,
                          next_question=Question.objects.get(question_number=10))
    Answer.objects.create(question=Question.objects.get(question_number=9),
                          answer_text="О выдаче лица",
                          score=-1)

    Answer.objects.create(question=Question.objects.get(question_number=10),
                          answer_text="10 суток",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=10),
                          answer_text="30 суток",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=10),
                          answer_text="40 суток",
                          score=1,
                          next_question=Question.objects.get(question_number=11))

    Answer.objects.create(question=Question.objects.get(question_number=11),
                          answer_text="Сообщает в Министерство иностранных дел Республики Беларусь о принятом решении",
                          score=1)
    Answer.objects.create(question=Question.objects.get(question_number=11),
                          answer_text="Передает материал территориальному ОВД",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=11),
                          answer_text="Осуществляет экстрадиционную проверку",
                          score=1,
                          next_question=Question.objects.get(question_number=12))

    Answer.objects.create(question=Question.objects.get(question_number=12),
                          answer_text="Осуществляют проверку по материалу, зарегистрированному в ЕК, и ОРМ по установлению местонахождения лица",
                          score=1,
                          next_question=Question.objects.get(question_number=13))
    Answer.objects.create(question=Question.objects.get(question_number=12),
                          answer_text="Не осуществляют иных ОРМ и процессуальных действий",
                          score=-1)

    Answer.objects.create(question=Question.objects.get(question_number=13),
                          answer_text="Нет",
                          score=-2)
    Answer.objects.create(question=Question.objects.get(question_number=13),
                          answer_text="Да (постановлением начальника ОВД)",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=13),
                          answer_text="Да (рапортом сотрудника)",
                          score=1,
                          next_question=Question.objects.get(question_number=14))

    Answer.objects.create(question=Question.objects.get(question_number=14),
                          answer_text="Нет",
                          score=-1)
    Answer.objects.create(question=Question.objects.get(question_number=14),
                          answer_text="Да",
                          score=1)


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0013_remove_answer_is_last_answer_in_game'),
    ]

    operations = [
        migrations.RunPython(init_questions),
    ]
