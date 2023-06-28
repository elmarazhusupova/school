from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, add_grade, send

urlpatterns = [
    path('/list', StudentListView.as_view(), name='student-list'),
    path('/add_grade/', add_grade, name='add-grade'),
    path('/create/', StudentCreateView.as_view(), name='student-create'),
    path('/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('/send/', send, name='send_email')
]
