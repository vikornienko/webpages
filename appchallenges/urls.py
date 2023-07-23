from django.urls import path

from .views import mounthly_challenges, mounthly_challenge_by_number, index

app_name = "appchallenges"

urlpatterns = [
    path("", index),
    path("<int:mounth>/", mounthly_challenge_by_number),
    path("<str:mounth>/", mounthly_challenges, name="challengemounth"),
]

