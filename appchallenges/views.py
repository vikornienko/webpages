from django.shortcuts import render  # noqa: F401
from django.urls import reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404

 
monthly_chall = {
    "january": "Eat many meat and drink much beer!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Hard learn Django Framework!",
    "april": "Hard learn Django Framework!",
    "may": "Eat many meat and drink much beer!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Hard learn Django Framework!",
    "august": "Eat many meat and drink much beer!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Hard learn Django Framework!",
    "november": "Eat many meat and drink much beer!",
    "december": "Walk for at least 20 minutes every day!",
}

def index(request):
    months = list(monthly_chall.keys())
    
    return render(request, "appchallenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_chall.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    forward_month = months[month - 1]
    """
    В функции reverse обязательно перед наименованием маршрута указывать имя приложения!
    Например, как в данном случае - "appchallenges:challengemonth"
    """
    redirect_path = reverse("appchallenges:challengemonth", args=(forward_month,))
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_chall[month]
        return render(request, "appchallenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        
    except:  # noqa: E722
        raise Http404()
    
