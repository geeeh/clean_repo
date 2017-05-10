import http.client
import json
import sys



def post_httpclient_app(url, inputs):
            
        try:        
            conn = http.client.HTTPSConnection(url)
            headers = {'Content-type': "application/json"}
            vars = {'text': inputs}
            my_vars = json.dumps(vars)
            conn.request("POST", '/markdown', my_vars, headers)

            response = conn.getresponse()
            return ("status code: " + str(response.status) + "\ndata: " + response.read().decode())
        except:
            return "site doesnt allow post"
            
url=input("url: ")
inputs=input("\npost inputs: ")
print(post_httpclient_app(url,inputs ))

while not inputs=="exit":
    inputs=input("\npost inputs: ")
    print(post_httpclient_app(url,inputs ))
exit()