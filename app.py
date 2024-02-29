import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests
from state_generator import generate_random_string


load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

login_url = "https://github.com/login/oauth/authorize"
access_token_url = "https://github.com/login/oauth/access_token"
redirect_uri = "http://localhost:8000/callback"

app = FastAPI()

@app.get("/")
async def request_identity():
    state = generate_random_string()
    parameters = {"client_id": client_id, "redirect_uri": redirect_uri, "login": "", "scope": "repo", "state": state, "allow_signup": True}
    redirect_url = login_url + "?" + "&".join([f"{k}={v}" for k, v in parameters.items()]) # this line from chatgpt
    return RedirectResponse(url=redirect_url) # this line from chatgpt

@app.get("/callback")
async def get_token(code, state):
    headers={"Accept": "application/json"}
    parameters = {"client_id": client_id, "client_secret": client_secret, "code": code}
    response = requests.post(url=access_token_url, params=parameters, headers=headers)
    response_data = response.json()
    access_token = response_data["access_token"]
    scope = response_data["scope"]
    token_type = response_data["token_type"]
    return "access_token: "+access_token+", scope: "+scope+", token_type: "+token_type