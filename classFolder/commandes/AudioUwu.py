from classFolder.Commande import Commande
from classFolder.ObsWebSocket import ObsWebSocket


class AudioUwu(Commande):
    regex = "^!uwu$"

    # the execution of commande.
    async def execute(self, client, message):
        #pass

        # todo : inclure an enum in block web socket for eatch type of call ?.
        # or a way to ask a specifique execution with parameters.

        obs = ObsWebSocket()
        obs.connect(client)
        obs.debug()
        obs.playAudio("uwu")  # bug hear -> can't print object with all details.
        obs.close()  # bug hear -> client is NoneType (connection to obs fail), and bug when try to close.