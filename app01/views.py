from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import HttpResponse
import logging
import json

logger = logging.getLogger(__name__) 

def testjson(request):
    # logger.info("请求来源: {}".format(request.headers["User-Agent"]))
    data = {
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
    }
    return HttpResponse(json.dumps(data))
