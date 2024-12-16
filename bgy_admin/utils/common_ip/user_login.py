from utils.common_ip.get_ip import search_ip


def get_user_login(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    login_browser = request.META.get('HTTP_SEC_CH_UA').split(';')[0][1:-1]
    login_os = request.META.get('HTTP_SEC_CH_UA_PLATFORM')[1:-1]
    login_location = search_ip(ip).get('addr')
    login_result = {
        'ip': ip,
        'login_browser': login_browser,
        'login_os': login_os,
        'login_location': login_location
    }
    return login_result
