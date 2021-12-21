"""
DocString:
Automate the testing of this API within 2 hours https://developer.nexmo.com/api/conversation. You may need to create a JWT token first here https://developer.nexmo.com/jwt.
Automating the whole https://developer.nexmo.com/api/conversation API will take a lot of time. Part of the task is to figure out testing of which API calls would cover most functionality, and focus just on them. It is not expected that everything in the API will get covered in 2 hours that you work on this task.
We will look for a readable code, tests that do not depend on each other, tests that clearly manifest their purpose. In case of failed test cases - the produced logs should provide information describing what went wrong.
It is OK to keep working on the task longer, but this may lower your score slightly. The idea is not to automate the testing of some API that we will never use, but to show your approach to a vaguely defined task of a similar nature.
Some information may seem missing in this task. This is intentional and you are expected to figure out what to do as part of this test.
"""

import requests ### for API testing
import pytest ## is the framework

@pytest.fixture ### Used for Suite Setup and Suite Teardown
def setup():
    print("Suite Setup - You can Set all Pre-requisite required for your test suite")
    yield
    print("Suite Tear Down - You can mention Clean Up Part here")


@pytest.mark.Smoke ### This is a custom marker.
def Test_ConversationGet():
    cookies = {
        'BCSI-CS-366981c10c8e7095': '1',
    }

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMDI2MDksImV4cCI6MTY0MDEyNDIwOSwianRpIjoiRzJyUE9yUlBUY2NFIiwiYXBwbGljYXRpb25faWQiOiJiNjhlYjU1MS04YTY5LTQ1MWEtOWYxYS05NjFiOWY1MjIzMzYifQ.wVSFb0H5q4pkn7VCHMsChwbLKyh0LmLVoaEkTgj-NIEwSAu7J8OV0dpv_QKZVyhtXpiE1L0YgM3AnHgixtIocIytnDzcALgue4z1nONrQ6gvTaIHzBzKJeBiJg2tY3xAPQC6KMwwYLJ3ajufi6dYvkUpMdXMsNfLacLjBNqnuBAFEXjXu-EoTHdW6NDVqoJFPzPWP1QwEouT4Om3bTr-40WjNPH1xyfRKcFQp_GL49YYxOkwb2QsO-O0Y5WASKmE6cctqd46BgmcJvOC37TRobgh-y1sfOzwQNqp_jOmfL2JIgB0GrwaNrP0wDupXGvDhmzqp3_E4GXrvcBMf9GDiQ',
        'Content-Type': 'text/plain',
    }

    data = {
        'api_key': '7e3a658f',
        'api_secret': 'VliqmFeHM7R4L8Md',
        'from': 'AcmeInc',
        'to': '447700900000',
        'text': 'Hello World!',
        'ttl': '900000',
        'callback': 'https://example.com/sms-dlr',
        'type': 'text',
        'body': '0011223344556677',
        'udh': '06050415811581',
        'protocol-id': '127',
        'title': 'Welcome',
        'url': 'https://example.com',
        'validity': '300000',
        'client-ref': 'my-personal-reference',
        'account-ref': 'customer1234',
        'entity-id': '1101456324675322134',
        'content-id': '1107457532145798767'
    }

    response = requests.get('https://api.nexmo.com/v0.1/conversations', headers=headers, cookies=cookies, data=data)
    assert response.status_code == 200, "Passed"
    print (response)

@pytest.mark.Smoke ### This is a custom marker.
def Test_ConversationGet():
    cookies = {
        'BCSI-CS-366981c10c8e7095': '1',
    }

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMDI2MDksImV4cCI6MTY0MDEyNDIwOSwianRpIjoiRzJyUE9yUlBUY2NFIiwiYXBwbGljYXRpb25faWQiOiJiNjhlYjU1MS04YTY5LTQ1MWEtOWYxYS05NjFiOWY1MjIzMzYifQ.wVSFb0H5q4pkn7VCHMsChwbLKyh0LmLVoaEkTgj-NIEwSAu7J8OV0dpv_QKZVyhtXpiE1L0YgM3AnHgixtIocIytnDzcALgue4z1nONrQ6gvTaIHzBzKJeBiJg2tY3xAPQC6KMwwYLJ3ajufi6dYvkUpMdXMsNfLacLjBNqnuBAFEXjXu-EoTHdW6NDVqoJFPzPWP1QwEouT4Om3bTr-40WjNPH1xyfRKcFQp_GL49YYxOkwb2QsO-O0Y5WASKmE6cctqd46BgmcJvOC37TRobgh-y1sfOzwQNqp_jOmfL2JIgB0GrwaNrP0wDupXGvDhmzqp3_E4GXrvcBMf9GDiQ',
        'Content-Type': 'text/plain',
    }

    data = {
        'api_key': '7e3a658f',
        'api_secret': 'VliqmFeHM7R4L8Md',
        'from': 'AcmeInc',
        'to': '447700900000',
        'text': 'Hello World!',
        'ttl': '900000',
        'callback': 'https://example.com/sms-dlr',
        'type': 'text',
        'body': '0011223344556677',
        'udh': '06050415811581',
        'protocol-id': '127',
        'title': 'Welcome',
        'url': 'https://example.com',
        'validity': '300000',
        'client-ref': 'my-personal-reference',
        'account-ref': 'customer1234',
        'entity-id': '1101456324675322134',
        'content-id': '1107457532145798767'
    }

    response = requests.get('https://api.nexmo.com/v0.1/conversations', headers=headers, cookies=cookies, data=data)
    assert response.status_code == 200, "Passed"
    print (response)
