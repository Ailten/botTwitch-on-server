from classFolder.Commande import Commande
from classFolder.ObsWebSocket import ObsWebSocket


class AudioUwu(Commande):
    regex = "^!uwu$"

    # the execution of commande.
    async def execute(self, client, message):

        # todo : inclure an enum in block web socket for eatch type of call ?.
        # or a way to ask a specifique execution with parameters.

        obs = ObsWebSocket()
        obs.connect(client)
        obs.playAudio("uwu")
        obs.close()