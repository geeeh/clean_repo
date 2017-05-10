import http.client
import json

def post_httpclient_app(url, input):
    try:
    
        conn = http.client.HTTPSConnection(url)
        headers = {'Content-type': "application/json"}
        vars = {'text': input}
        my_vars = json.dumps(vars)
        conn.request("POST", '/markdown', my_vars, headers)

        response = conn.getresponse()
        return (str(response.status) + "\n" + response.read().decode())
    except:
        return "oops! an error occured"


#print(post_httpclient_app("api.github.com", "assfs"))