from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app/agent', views.register_agent),
    url(r'^app/auth', views.authenticate_agent),
    url(r'^app/sites/list/?agent={agentId}', views.get_todo_items),
    url(r'^app/sites?agent={agentId}', views.save_todo_items),
]
