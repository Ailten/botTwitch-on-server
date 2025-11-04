from classFolder.Commande import Commande


class AudioUwu(Commande):
    regex = "^!uwu$"

    # the execution of commande.
    async def execute(self, client, message):

        await client.callObs("instruction-obs-web-socket")