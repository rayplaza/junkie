from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('records/', views.RecordList.as_view(), name='records_index'),
    path('records/<int:pk>/', views.RecordDetail.as_view(), name='records_detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_photo/', views.add_photo, name='add_photo'),
]