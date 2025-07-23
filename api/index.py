import sys
sys.path.append('..')

from app import app

def handler(request):
    return app(request)
