from classFolder.Commande import Commande


class Hello(Commande):
    regex = "^!hello"

    # the execution of commande.
    async def execute(self, client, message):

        await message.channel.send("Hello !")

