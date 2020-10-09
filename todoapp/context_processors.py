from .util import get_project

def project_processor(request):
    return {'PROJECT': get_project(request)}
