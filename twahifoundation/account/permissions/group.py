from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name__in=group_names):
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)


class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if len(set(user_groups).intersection(self.group_required)) <= 0:
            raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
