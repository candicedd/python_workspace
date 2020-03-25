import http.client

conn = http.client.HTTPConnection("localhost", 8080)
conn.request("GET", "/random-number")
res = conn.getresponse()
content = res.read().decode()
print(content)
