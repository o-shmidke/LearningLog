from django.http import Http404


def _check_topic_owner(request, topic):
    """Проверяет является ли пользователь собственником тем"""
    if topic.owner != request.user:
        raise Http404
