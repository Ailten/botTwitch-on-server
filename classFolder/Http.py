import requests

class Http:

    @staticmethod
    async def askForNewAccessToken(currentTokenObj):

        # DOC : https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#client-credentials-grant-flow

        url = "https://id.twitch.tv/oauth2/token"
        objJson = {
            "client_id": currentTokenObj["bot"]["idClient"],
            "client_secret": currentTokenObj["bot"]["secretClient"],
            "grant_type": "client_credentials"
        }

        responce = requests.post(url, json = objJson)

        if(not responce.ok):
            print(f"error in http ask token : {responce.text}")
            raise Exception(f"http request token : {responce.reason}")

        #print(responce.text)

        return responce.json()


    @staticmethod
    async def callAnotherScript(client, payload):

        payload["from"] = 'botTwitch'

        return requests.post(f"http://127.0.0.1:5000/event/{payload['event']}", json=payload)


