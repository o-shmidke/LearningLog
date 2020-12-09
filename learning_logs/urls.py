"""Определяет схему URL для lerning_logs"""

from django.urls import path, include

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Full information about tropic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page of Add new tropic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page of Add new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page of Edit the entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]