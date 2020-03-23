from behave import given, when, then, step
import requests
import base64

api_endpoints = {}
request_headers = {}
auth_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
snippetid_userid = {}
api_url=None

# START POST Scenario
@given(u'I set POST snippet api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url
    print('url :'+ api_endpoints['POST_URL'])

@when(u'I set auth_header param username as "{username}"')
def step_impl(context, username):
    auth_headers['username'] = str(username)
    print('username :'+ str(username))

@when(u'I set auth_header param password as "{password}"')
def step_impl(context, password):
    auth_headers['password'] = str(password)
    print('password :'+ str(password))

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I set request Body')
def step_impl(context):
    
    request_bodies['POST']={"title": "BDDTestCreateSnippet",
                            "code": "Snippet snippet=new Snippet()",
                            "linenos": 'false', 
                            "language": "python", 
                            "style": "friendly"}

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I send a POST HTTP request')
def step_impl(context):
    #AUTH = requests.auth.HTTPBasicAuth("app_user1", "app_user1")
    AUTH = requests.auth.HTTPBasicAuth(auth_headers['username'], auth_headers['password'])
    # sending get request and saving response as response object
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], auth=AUTH)
    #response = requests.post(url=api_endpoints['POST_URL']) #http://localhost:8000/snippets/
    
    # extracting response text
    response_texts['POST']=response.text
    print("POST RESPONSE :"+ response.text)
    # extracting response status_code
    statuscode = response.status_code
    print("POST RESPONSE STATUS CODE :"+ str(statuscode))
    response_codes['POST'] = statuscode
    if statuscode == 201:
        print("Snippet id created = " + str(response.json().get('id')))
        print("Snippet owner created = " + response.json().get('owner'))
        id = str(response.json().get('id'))
        owner = response.json().get('owner')
        snippetid_userid['id'] = id
        snippetid_userid['owner'] = owner

@then(u'I receive valid HTTP response code 201 for POST')
def step_impl(context):
    print('Post response code : '+ str(response_codes['POST']))
    assert response_codes['POST'] is 201

@then(u'Response BODY POST is non-empty')
def step_impl(context):
    assert response_texts['POST'] is not None
# END POST Scenario

# START GET Scenario
@given(u'I set snippets REST API url')
def step_impl(context):
    global api_url    
    api_url = 'http://localhost:8000/snippets/'

# START GET Scenario
@given(u'I set GET snippet api endpoint with id of snippet created in POST scenario')
def step_impl(context):
    snippet_id = snippetid_userid['id']
    #api_endpoints['GET_URL'] = api_url + id
    api_endpoints['GET_URL'] = api_url + snippet_id
    print('url :'+ api_endpoints['GET_URL'])

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I send GET HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.get(url=api_endpoints['GET_URL']) #http://localhost:8000/snippets
    print('Response Text = ' + str(response.text))
    # extracting response text
    response_texts['GET']=response.text
    # extracting response status_code
    statuscode = response.status_code
    print('Response Status Code = ' + str(statuscode))
    response_codes['GET'] = statuscode

@then(u'I receive valid HTTP response code 200 for "{request_name}"')
def step_impl(context,request_name):
    print('Get response code for '+ request_name +':'+ str(response_codes[request_name]))
    assert response_codes[request_name] is 200

@then(u'Response BODY "{request_name}" is non-empty')
def step_impl(context,request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None
# END GET Scenario


# START PUT Scenario
@given(u'I set PUT snippet api endpoint with id of snippet created in POST scenario')
def step_impl(context):
    snippet_id = snippetid_userid['id']
    #api_endpoints['GET_URL'] = api_url + id
    api_endpoints['PUT_URL'] = api_url + snippet_id + "/"
    print('url for PUT :'+ api_endpoints['PUT_URL'])

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I set request Body for PUT')
def step_impl(context):    
    #request_bodies['PUT']={"title": "BDDTestUPDATESnippetwith500tatuscode",
                           #"code": "New code for BDD Update/PUT"}
    request_bodies['PUT']={"title": "foo","code": "BDDUpdate"}

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I send a PUT HTTP request with the same credentials as in POST scenario')
def step_impl(context):
    AUTH = requests.auth.HTTPBasicAuth(auth_headers['username'], auth_headers['password'])
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], auth=AUTH)
    # extracting response text
    response_texts['PUT'] = response.text
    print("update response :" + response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['PUT'] = statuscode    

@then(u'I receive valid HTTP response code 200 for PUT')
def step_impl(context):
    print('PUT response code : '+ str(response_codes['PUT']))
    assert response_codes['PUT'] is 200

@then(u'Response BODY PUT is non-empty')
def step_impl(context):
    assert response_texts['PUT'] is not None
# END PUT Scenario


# START PUT Scenario with unauthorized credentials ( different than in Post scenario )

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I send a PUT HTTP request with snippet id created in POST scenario for unauthorized user app_user2/app_user2')
def step_impl(context):
    AUTH = requests.auth.HTTPBasicAuth("app_user2", "app_user2")
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], auth=AUTH)
    # extracting response text
    response_texts['PUT'] = response.text
    print("update response :" + response.text)
    failure_text = str(response.json().get('detail'))
    response_codes['PUT'] = failure_text 

@then(u'I receive valid error message PUT for unauthorized user')
def step_impl(context):
    print('PUT response message : '+ response_codes['PUT'])
    assert response_codes['PUT'] == "You do not have permission to perform this action."

# END PUT Scenario with unauthorized credentials ( different than in Post scenario )


# START DELETE Scenario with unauthorized credentials ( different than in Post scenario )

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'I send a DELETE HTTP request with snippet id created in POST scenario')
def step_impl(context):
    AUTH = requests.auth.HTTPBasicAuth(auth_headers['username'], auth_headers['password'])
    response = requests.delete(url=api_endpoints['PUT_URL'], auth=AUTH)
    # extracting response text
    response_texts['DELETE'] = response.text
    print("DELETE response :" + str(response.text))
    # extracting response status_code
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode  

@then(u'I receive valid http code 204 No Content')
def step_impl(context):
    print('DELETE response code : '+ str(response_codes['DELETE']))
    assert response_codes['DELETE'] is 204

# END DELETE Scenario with unauthorized credentials ( different than in Post scenario )