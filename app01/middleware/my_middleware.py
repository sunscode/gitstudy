from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
import re

from istudy import settings


class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # 需要登录后访问的地址   也就是说 需要判断登录状态
        # 默认所有的地址都需要登录才能访问
        # 设置一个白名单  不登录就能访问
        url = request.path_info
        print(url)
        # 白名单
        for i in settings.WHITE_LIST:
            if re.match(i, url):
                return

        # 校验登录状态
        is_login = request.session.get('is_login')
        # print(is_login)
        if is_login:
            # 已经登录了  可以访问
            return
            # 没有登录的话 需要去登录
        return redirect("{}?url={}".format(reverse('login'), url))
