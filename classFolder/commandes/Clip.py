from classFolder.Commande import Commande
import datetime


class Clip(Commande):
    regex = "^!clip"

    lastTimeCalled: datetime.datetime.now()
    cooldown: 15

    # the execution of commande.
    async def execute(self, client, message):

        # compare cooldown time.
        isCooldownValid = (datetime.datetime.now() - self.lastTimeCalled).total_seconds() > self.cooldown

        # is cooldown unvalid, error.
        if(not isCooldownValid):
            await message.channel.send("un clip à déja été créé récement.")
            return

        # update time for next cooldown.
        self.lastTimeCalled = datetime.datetime.now()
        
        # try make clip.
        try:
            await client.clip()
        except:
            await message.channel.send("le clip n'a pas pu être créé.")
            return

        # print validation for making clip.
        await message.channel.send("le clip à été créé !")

