from django.shortcuts import render  # noqa: F401
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    list_items = ""
    months = list(monthly_chall.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("appchallenges:challengemounth", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def mounthly_challenge_by_number(request, month):
    months = list(monthly_chall.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid mounth")
    
    forward_month = months[month - 1]
    """
    В функции reverse обязательно перед наименованием маршрута указывать имя приложения!
    Например, как в данном случае - "appchallenges:challengemounth"
    """
    redirect_path = reverse("appchallenges:challengemounth", args=(forward_month,))
    return HttpResponseRedirect(redirect_path)


def mounthly_challenges(request, mounth):
    try:
        challenge_text = monthly_chall[mounth]
        return HttpResponse(challenge_text)
    except:  # noqa: E722
        return HttpResponseNotFound("Not supported!") 
    
