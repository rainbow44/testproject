
from django.urls import path

from shop import views

urlpatterns = [
    path("", views.mainPage),
    path("<slug:category_id>", views.categoryView),
    path("forms/", views.formsPage),
    path("forms/completed/", views.formCompleted, name="completed_form_page"),
    path("<slug:category_id>/<int:id>",views.showProduct)
]
