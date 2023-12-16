# Simple GET request Number 1
import requests

url = "https://randomuser.me/api"

# making a GET request
response = requests.get(url)

print('URL: ', response.url) # print the URL
print('Status code: ', response.status_code) # print the HTTP status code
print('HTTP header: ', response.headers) # print the headers
print(response.content) # print content of the response
print(response.json()) # print the JSON data
# print(response.text) # print the HTML codes





# Simple POST request Number 2
import requests

url = 'https://httpbin.org/post'

payload = {
  'name':'Hussain',
  'last-name':'Erfani',
  'website':'http://herfani.epizy.com/'
}

# making a POST request
r = requests.post(url, data=payload)
print(r.status_code) # HTTP status code
print(r.json()) # JSON data