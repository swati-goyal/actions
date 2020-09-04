import requests

url = "https://madrid.quintype.io/"
path = "ampstories/visual-stories/why-you-need-a-dog-in-your-life"
resp = requests.get(url+path)

print(resp.text)
