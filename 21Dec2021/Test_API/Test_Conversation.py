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
def test_ConversationGet(setup):
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMzQ2OTIsImV4cCI6MTY0MDczOTQ5MiwianRpIjoicnhmREIwdHhKQ3JTIiwiYXBwbGljYXRpb25faWQiOiJiNjhlYjU1MS04YTY5LTQ1MWEtOWYxYS05NjFiOWY1MjIzMzYifQ.1xMX84PaEFOWsBK1kF5i8upqESNu85icT1h_tUZ2ozptwWtrTwJ4U-ddH4SX9nGCxVoQ56wLprpc_tYg2zMxJFHU7-yL0Ihref8ZW3OWnJf3CJLc8f-GwLC8AoWVri7MnkHZGnpn67mP4EGHK-6Gp1czKA0GpAkXK14U_XRT_jaB1_XQbAoKODsRPYCGodAJq2d-FLquB5wkIWuIHY-eJMKu3KJdKxoBxrIgSyN3SlUkINuyXzP4DcA0KTlUTk6OGgn9Ogild2Cee1xoqH60oVsf34kw2zsOYm1gnCRRhH0YHqIvKcZik9pXO5mbV-FEUDAZ5U1xn_UZOpNmWmQaCw',
    }

    response = requests.get('https://api.nexmo.com/v0.1/conversations', headers=headers)
    print(response)
    assert response.status_code == 200, "Got the 200 response code"

@pytest.mark.Smoke ### This is a custom marker.
def test_ConversationPost(setup):
    import requests

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMzQ2OTIsImV4cCI6MTY0MDczOTQ5MiwianRpIjoicnhmREIwdHhKQ3JTIiwiYXBwbGljYXRpb25faWQiOiJiNjhlYjU1MS04YTY5LTQ1MWEtOWYxYS05NjFiOWY1MjIzMzYifQ.1xMX84PaEFOWsBK1kF5i8upqESNu85icT1h_tUZ2ozptwWtrTwJ4U-ddH4SX9nGCxVoQ56wLprpc_tYg2zMxJFHU7-yL0Ihref8ZW3OWnJf3CJLc8f-GwLC8AoWVri7MnkHZGnpn67mP4EGHK-6Gp1czKA0GpAkXK14U_XRT_jaB1_XQbAoKODsRPYCGodAJq2d-FLquB5wkIWuIHY-eJMKu3KJdKxoBxrIgSyN3SlUkINuyXzP4DcA0KTlUTk6OGgn9Ogild2Cee1xoqH60oVsf34kw2zsOYm1gnCRRhH0YHqIvKcZik9pXO5mbV-FEUDAZ5U1xn_UZOpNmWmQaCw',
        'Content-Type': 'application/json',
    }

    data = '{\n  "name": "customer_chat",\n  "display_name": "Customer Chat",\n  "image_url": "https://example.com/image.png",\n  "properties": {\n    "ttl": 60\n  }\n}'

    response = requests.post('https://api.nexmo.com/v0.1/conversations', headers=headers, data=data)
    assert response.status_code == 200, "Passed"
    print(response)

@pytest.mark.skip  ### This is a custom marker.
def test_ConversationPut(setup):
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMzQ2OTIsImV4cCI6MTY0MDczOTQ5MiwianRpIjoicnhmREIwdHhKQ3JTIiwiYXBwbGljYXRpb25faWQiOiJiNjhlYjU1MS04YTY5LTQ1MWEtOWYxYS05NjFiOWY1MjIzMzYifQ.1xMX84PaEFOWsBK1kF5i8upqESNu85icT1h_tUZ2ozptwWtrTwJ4U-ddH4SX9nGCxVoQ56wLprpc_tYg2zMxJFHU7-yL0Ihref8ZW3OWnJf3CJLc8f-GwLC8AoWVri7MnkHZGnpn67mP4EGHK-6Gp1czKA0GpAkXK14U_XRT_jaB1_XQbAoKODsRPYCGodAJq2d-FLquB5wkIWuIHY-eJMKu3KJdKxoBxrIgSyN3SlUkINuyXzP4DcA0KTlUTk6OGgn9Ogild2Cee1xoqH60oVsf34kw2zsOYm1gnCRRhH0YHqIvKcZik9pXO5mbV-FEUDAZ5U1xn_UZOpNmWmQaCw',
        'Content-Type': 'application/json',
    }
    data = '{\n  "name": "customer_chat123",\n  "display_name": "Customer Chat",\n  "image_url": "https://example.com/image.png",\n  "properties": {\n    "ttl": 60\n  }\n}'
    response = requests.put('https://api.nexmo.com/v0.1/conversations/CON-1db1eb63-76f0-43d3-9e17-5891fbf0643f',
                            headers=headers, data=data)

    print(response)
    assert response.status_code != 200, "Failed Put Operation Failed"

### Run above testcases using command:  pytest -rA Test_Conversation.py --html="report.html" -s
