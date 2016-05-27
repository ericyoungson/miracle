import os

from pyramid.response import (
    FileResponse,
    Response,
)

HERE = os.path.dirname(__file__)
STATIC_DIR = os.path.abspath(os.path.join(HERE, os.pardir, 'static'))
VERSION_FILE = os.path.join(STATIC_DIR, 'version.json')


def configure(config):
    config.add_view(heartbeat_view,
                    name='__heartbeat__', renderer='json')
    config.add_view(lbheartbeat_view,
                    name='__lbheartbeat__', renderer='json')

    config.add_view(index_view)
    config.add_view(robotstxt_view, name='robots.txt')
    config.add_view(version_view, name='__version__')


def heartbeat_view(request):
    return {}


_index_response = Response(content_type='text/plain', body='''\
It works!
''')


def index_view(request):
    return _index_response


def lbheartbeat_view(request):
    return {'status': 'OK'}


_robots_response = Response(content_type='text/plain', body='''\
User-agent: *
Disallow: /__heartbeat__
Disallow: /__lbheartbeat__
Disallow: /__version__
''')


def robotstxt_view(context, request):
    return _robots_response


def version_view(request):
    return FileResponse(
        VERSION_FILE,
        content_type='application/json',
        request=request)
