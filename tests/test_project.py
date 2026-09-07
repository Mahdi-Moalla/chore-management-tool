"""Test project setup."""


def test_database_connection(db):
    """Verify Django and SQLite connection works."""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        
    assert True, "Basic functionality works"
