from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
import json
from .models import CustomerRequests

# Create your views here.
def customerrequests(request:HttpRequest) -> HttpResponse:

    if request.method == "GET":
        custRequests = CustomerRequests.objects.all()
        serialized_requests = [custRequest.cust_req_code for custRequest in custRequests]
        return HttpResponse(json.dumps(serialized_requests))

    if request.method == "POST":
        body = json.loads(request.body)
        customerRequests = CustomerRequests(
            cust_req_code = body['cust_req_code'],
            # facility_req_type_id = 1,
            # facility_id = 1,
            # unit_id = 1,
            # person_id = 1,
            request_date = '2024-10-11',
            request_json ='{}',
            crt_rsn = "new req",
            crt_by = "sarika")
        customerRequests.save()
        return HttpResponse(json.dumps({'id':customerRequests.id, 'code' : customerRequests.cust_req_code}))


def customer_request(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "GET":
        custReq = get_object_or_404(CustomerRequests, id=id)
        return HttpResponse(json.dumps({'id': custReq.id, 'code': custReq.cust_req_code}))

    if request.method == "PUT":
        body = json.loads(request.body)
        # custReq = CustomerRequests.objects.get(id=id)
        custReq = get_object_or_404(CustomerRequests, id=id)
        custReq.cust_req_code = body['cust_req_code']
            # facility_req_type_id = 1,
            # facility_id = 1,
            # unit_id = 1,
            # person_id = 1,
        custReq.request_date = '2024-10-11'
        custReq.request_json ='{}'
        custReq.crt_rsn = "new req"
        custReq.crt_by = "sarika"
        custReq.save()
        return HttpResponse(json.dumps({'id':custReq.id, 'code' : custReq.cust_req_code}))

    if request.method == "DELETE":
        # custReq = CustomerRequests.objects.get(id=id)
        custReq = get_object_or_404(CustomerRequests, id=id)
        custReq.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))