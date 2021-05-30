from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
	path("", views.index, name="index"),
	# path("<str:slug>/", views.question_view, name="question_page"),
	# path("signup/", views.signup, name="signup"),
	# path("login/", views.login, name="login"),
]