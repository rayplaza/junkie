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
    path('comics/', views.ComicList.as_view(), name='comics_index'),
    path('comics/<int:pk>/', views.ComicDetail.as_view(), name='comics_detail'),
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
]