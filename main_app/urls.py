from django.urls import path
from . import views

urlpatterns = [
    path('', views.PrintList.as_view(), name ="print_list"),
    path('about/', views.About.as_view(), name="about"),
    path('prints/new/',  views.PrintCreate.as_view(), name="print_create"),
    path('prints/<int:pk>/', views.PrintDetail.as_view(), name="print_detail"),
    path('prints/<int:pk>/update',views.PrintUpdate.as_view(), name="print_update"),
    path('prints/<int:pk>/delete',views.PrintDelete.as_view(), name="print_delete"), 
    path('prints/<int:pk>/cards/new/', views.CardCreate.as_view(), name="card_create"),
    path('prints/<int:pk>/mugs/new/', views.MugCreate.as_view(), name="mug_create"),
    path('prints/<int:pk>/photos/new/', views.PhotoCreate.as_view(), name="photo_create"),
    path('prints/<int:pk>/puzzles/new/', views.PuzzleCreate.as_view(), name="puzzle_create"),

]


