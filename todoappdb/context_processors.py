from .settings import PORTAL_URL

def todoapp_proc(request):
    return {'PORTAL_URL': PORTAL_URL}