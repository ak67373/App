from django.conf.urls import url
from .views import register_agent, authenticate_agent, get_todo_items, save_todo_items

urlpatterns = [
    url(r'^app/agent', register_agent),
    url(r'^app/auth', authenticate_agent),
    url(r'^app/sites/list/?agent={agentId}', get_todo_items),
    url(r'^app/sites?agent={agentId}', save_todo_items),
]
