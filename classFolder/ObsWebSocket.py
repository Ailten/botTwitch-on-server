
from obswebsocket import obsws, requests #pip3 install obs-websocket-py


class ObsWebSocket:

    def __init__(self):
        self.client = None

    # connect to obs.
    def connect(self, bot):
        param = bot.getTokenObj()
        self.client = obsws(
            "http://" + param["obs"]["ip"],
            param["obs"]["port"],
            param["obs"]["password"]
        )

    # disconnect from obs.
    def close(self):
        if(self.client != None):
            self.client.disconnect()

    
    # play a audio layer.
    def playAudio(self, nameLayer):

        # todo: debug.

        print('...')
        #print(self.client)
        print(vars(self.client))
        print('...')


        #self.client.callback.register(on_input_mute_state_changed)

        #self.client.call(request.)

