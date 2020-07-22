from rest_framework.views import exception_handler
from .response import APIResponse
from .logging import log

def comm_exception_handler(exc,context):
    # log.error(f'{0},{1}'.format(str(context['view']),str(exc)))
    ret = exception_handler(exc,context)
    if not ret:
        return APIResponse(code=101,msg='error',result=str(exc))
        # drf处理不了，返回none给django处理的异常
        # 此处可以加额外逻辑
    else:
        return APIResponse(code=0,msg='error',result=ret.data)
