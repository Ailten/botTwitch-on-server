
from obswebsocket import obsws, requests #pip3 install obs-websocket-py


class ObsWebSocket:

    def __init__(self):
        self.client = None

    # connect to obs.
    def connect(self, bot):
        param = bot.getTokenObj()
        self.client = obsws(
            param["obs"]["ip"],
            param["obs"]["port"],
            param["obs"]["password"]
        )
        self.client.connect()

    # disconnect from obs.
    def close(self):
        if(self.client != None):
            self.client.disconnect()

    # debug client.
    def debug(self):
        print(vars(self.client))
    

    # play a audio layer.
    def playAudio(self, nameLayer):
        
        print("<-- playAudio -->")
        print(self.client.send("GetSceneList"))

        #self.client.callback.register(on_input_mute_state_changed)

        #self.client.call(request.)

