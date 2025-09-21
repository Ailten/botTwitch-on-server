from classFolder.Commande import Commande
import datetime


class ShootOut(Commande):
    regex = "^!so"

    lastTimeCalled: datetime.datetime.now()
    cooldown: 120

    # the execution of commande.
    async def execute(self, client, message):

        # verification for permission.
        if(message.author is None or not (message.author.is_mod or message.author.is_broadcaster)):
            await message.channel.send("vous n'avez pas les permission.")
            return

        # compare cooldown time.
        isCooldownValid = (datetime.datetime.now() - self.lastTimeCalled).total_seconds() > self.cooldown

        # is cooldown unvalid, error.
        if(not isCooldownValid):
            await message.channel.send("un so à déja été créé récement.")
            return

        # update time for next cooldown.
        self.lastTimeCalled = datetime.datetime.now()

        # get param (pseudo viewer to shootout).
        param = self.extractParams(message, isSplitBySpace=False)

        # get token.
        objToken = client.getTokenObj()

        # get users.
        users = await client.fetch_users(
            names=[param], 
            token=objToken["bot"]["appAccessToken"], 
            force=False
        )

        await client.shootOut(users[0].id)
        