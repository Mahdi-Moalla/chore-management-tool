#!/usr/bin/env python
import os, sys
sys.path.insert(0, 'src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
exec(open('src/config/django_setup.py').read() if False else '''
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
''')
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
