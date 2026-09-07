#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os, sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT / 'src'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def main():
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
