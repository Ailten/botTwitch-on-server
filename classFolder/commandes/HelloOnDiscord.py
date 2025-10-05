from classFolder.Commande import Commande


class Hello(Commande):
    regex = "^!helloDiscord$"

    # the execution of commande.
    async def execute(self, client, message):

        responce = client.callBotDiscord({
            'to': 'botDiscord',
            'event': 'helloDiscord', # type action todo.
            'data': { # data send (usefull for the event todo).
                'channelName': 'bot-log',
                'message': 'Hello ! (from twitch)'
            }
        })

        if responce.status_code == 200:
            await message.channel.send("Hello ! (success call discord)")
        else
            await message.channel.send(f"Error {responce.status_code}")
            print(responce)

