from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from luffyapi.utils.logging import log
from . import settings

def rand_code():
    import random
    rd_code = ''
    for i in range(4):
        rd_code += str(random.randint(0,9))
    return rd_code

def send_sms(phone,code):
    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = ["5678","3"]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone,
                                         settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        log.error(f'{phone}:短信发送失败,错误为{str(e)}')
