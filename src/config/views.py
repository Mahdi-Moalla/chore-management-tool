from django.http import HttpResponse
from django.db import connection

def start_app():
    """Initialize the application."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    return HttpResponse("Chore Management Tool Started")
