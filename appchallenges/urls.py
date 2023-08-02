from django.urls import path

from .views import monthly_challenges, monthly_challenge_by_number, index

app_name = "appchallenges"

urlpatterns = [
    path("", index, name="index"),
    path("<int:month>/", monthly_challenge_by_number),
    path("<str:month>/", monthly_challenges, name="challengemonth"),
]

