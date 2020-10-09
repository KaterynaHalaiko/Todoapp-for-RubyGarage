from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects, size, request, context, var_name='object_list'):
    """Paginate objects provided by view"""
    # apply pagination
    paginator = Paginator(objects, size)
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context

def get_project(request):
    """Returns list of existing groups"""
    # deferred import of Group model to avoid cycled imports
    from .models import Project

    # get currently selected project
    cur_project = get_current_project(request)

    project = []
    for project in Project.objects.all().order_by('title'):
        project.append({
            'id': project.id,
            'title': project.title,
            'leader': project.leader and (u'%s %s' % (project.leader.first_name,
                project.leader.last_name)) or None,
            'selected': cur_project and cur_project.id == project.id and True or False
        })
    return project

def get_current_project(request):
    """Returns currently selected group or None"""

    # we remember selected group in a cookie
    pk = request.COOKIES.get('current_project')

    if pk:
        from .models import Project
        try:
            project = Project.objects.get(pk=int(pk))
        except Project.DoesNotExist:
            return None
        else:
            return project
    else:
        return None
