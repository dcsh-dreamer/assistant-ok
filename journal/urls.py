from django.urls import path
from .views import *

urlpatterns = [
    path('', JournalList.as_view(), name="journal_list"), 
    path('create/', JournalCreate.as_view()),
    path('<int:pk>/update/', JournalUpdate.as_view()), 
    path('<int:pk>/delete/', JournalDelete.as_view()),
]