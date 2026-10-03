#TODO: Add this to the project.
#get the other wiki's data, and convert it into an easily parseable value set.
import requests
API = "https://megatenwiki.com/api.php"

def apiRequest(params):
    params["format"] = "json"