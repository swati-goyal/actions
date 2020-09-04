import requests

resp = requests.get("https://madrid.quintype.io/ampstories/visual-stories/why-you-need-a-dog-in-your-life")

print(resp.text)