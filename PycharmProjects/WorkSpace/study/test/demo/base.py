import requests

url = "http://test-web-carrier.ubor56.com"
interface = "/login"
requestUrl = url + interface
header = {
    'Content-Type': 'application/json'
}
requestParams = {
    "authType":0,
    "username":"xhxwlgs",
    "password":"111111",
    "deviceInfo":{
        "latitude":31.25072419,
        "longitude":121.63090162,
        "platform":2,
        "model":"iPhone XR",
        "sdkVersion":"14.6",
        "language":"ch",
        "brand":"iPhone",
        "cameraAuthorized":0,
        "version":"3.2.4",
        "locationAuthorized":0,
        "imeiCode":"C8B5495A-04C0-406B-A88B-92774E0195BB"
    }
}
timeout = 10
# get request exp
get_response = requests.get(url=requestUrl,headers=header, params=requestParams,timeout=timeout)
print(get_response.text)
print(get_response.json)

# post request exp
post_response = requests.post(url=requestUrl,headers=header, json=requestParams,timeout=timeout)
print(post_response.text)
print(post_response.json())