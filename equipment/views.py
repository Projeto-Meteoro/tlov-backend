from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from equipment.models import Data
import requests
# Create your views here.
import schedule
import time
import json
from equipment.serializer import DataSerializer
from rest_framework.parsers import JSONParser

def data_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        info = Data.objects.all()
        serializer = DataSerializer(info, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def set_ip_address(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        set_ip = request_data['ip']
        ipaddress = set_ip
        return JsonResponse(ipaddress)

def create_new_data():
    new_data = Data(power=30, equipment='Geladeira')
    new_data.save()
    # status = requests.get("http://192.168.81.137/status")
    # if status.status_code == 200:
    #    data = json.loads(status.content.decode('utf8').replace("'", '"'))
    #    power = data['meters'][0]['power']
    #   new_data = Data(power = power, equipment= 'Geladeira' )
    #    new_data.save()

def get_status(request):
    url = "https://shelly-66-eu.shelly.cloud/device/status"
    data = {'id': "c45bbe6c64dc",
            'auth_key': "MTg2OWQwdWlkDFA6B6EACDAB8BC84E33AD0BDC14EDF8679C4B20D3BF56A95FD20A4315B39ABD685253778554E9D6"
            }
    status = requests.get(url=url, params=data)

    if status.status_code == 200:
        data = json.loads(status.content.decode('utf8').replace("'", '"'))
        power = data['data']['device_status']['meters'][0]['power']
        relay = data['data']['device_status']['relays'][0]['ison']
        new_data = Data(power=power, equipment='Geladeira', status=relay)
        new_data.save()
        serializer = DataSerializer(new_data)
        return JsonResponse(serializer.data, safe=False)


def toggle_relay(request):
    info = Data.objects.last()
    status = "off" if info.status == True else "on"
    url = "https://shelly-66-eu.shelly.cloud/device/relay/control"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {'id': "c45bbe6c64dc",
            'auth_key': "MTg2OWQwdWlkDFA6B6EACDAB8BC84E33AD0BDC14EDF8679C4B20D3BF56A95FD20A4315B39ABD685253778554E9D6",
            'channel': 0,
            'turn': status}
    r = requests.post(url, data=data, headers=headers)
    return r




schedule.every(1).seconds.do(create_new_data)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

