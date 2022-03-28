from django.shortcuts import get_object_or_404, render, redirect

from .models import Schedule, Option


# главная страница со списком дел
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_schedule и message
    return render(
        request,
        "index.html",
        {
            "latest_schedule":
                Schedule.objects.order_by('-pub_date')[:5],
            "message": message
        }
    )


# страница загадки со списком ответов
def detail(request, schedule_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "answer.html",
        {
            "schedule": get_object_or_404(Schedule, pk=schedule_id),
            "error_message": error_message
        }
    )


# обработчик выбранного варианта ответа -
# сам не отдает страниц, а только перенаправляет (redirect)
# на другие страницы с передачей в GET-параметре
# сообщения для отображения на этих страницах
def answer(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    try:
        option = schedule.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return redirect(
            '/schedule/' + str(schedule_id) +
            '?error_message=Ничего не выбрано',
        )
    else:
        if option.correct:
            return redirect(
                "/schedule/?message=Отлично! Угадал, вспомни, какие еще задачи!")
        else:
            return redirect(
                '/schedule/' + str(schedule_id) +
                '?error_message=Неправильный ответ!',
            )
