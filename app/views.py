from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as httpstatus


@api_view(['POST', ])
def register_agent(request):
    agent_id = request.data.get("agent_id")
    password = request.data.get("password")
    from .service import register_agent
    register_agent(agent_id, password)
    return Response({'status_code': httpstatus.HTTP_200_OK, 'status': 'account created'}, httpstatus.HTTP_200_OK)


@api_view(['POST', ])
def authenticate_agent(request):
    agent_id = request.data.get("agent_id")
    password = request.data.get("password")
    from .service import authenticate_agent
    is_authentic, agent_id = authenticate_agent(agent_id, password)
    if is_authentic is True:
        return Response({'status_code': httpstatus.HTTP_200_OK, 'status': 'success', "agent_id": agent_id}, httpstatus.HTTP_200_OK)
    return Response({'status_code': httpstatus.HTTP_401_UNAUTHORIZED, 'status': 'failure'}, httpstatus.HTTP_401_UNAUTHORIZED)


@api_view(['GET', ])
def get_todo_items(request):
    agent_id = request.GET.get('agent')
    from .service import get_todo_items
    todo_items = get_todo_items(agent_id)
    return Response({'items': todo_items}, httpstatus.HTTP_200_OK)


@api_view(['POST', ])
def save_todo_items(request):
    agent_id = request.GET.get('agent')
    title = request.data.get("title")
    description = request.data.get("description")
    category = request.data.get("category")
    due_date = request.data.get("due_date")
    from .service import save_todo_item
    save_todo_item(agent_id, title, description, category, due_date)
    return Response({'status_code': httpstatus.HTTP_200_OK, 'status': 'success'}, httpstatus.HTTP_200_OK)
