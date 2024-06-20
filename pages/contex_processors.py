def get_group(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
        user_groups_string = ','.join(user_groups)
    else:
        user_groups_string = ''
    return {'user_groups_string': user_groups_string}
