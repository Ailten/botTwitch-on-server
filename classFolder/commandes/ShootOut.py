from classFolder.Commande import Commande
import datetime


class ShootOut(Commande):
    regex = "^!so [@]{0,1}[a-zA-Z0-9]{3,}$"

    lastTimeCalled: datetime.datetime.now()
    cooldown: 120

    # the execution of commande.
    async def execute(self, client, message):

        # verification for permission.
        if(message.author is None or not (message.author.is_mod or message.author.is_broadcaster)):
            await message.channel.send("vous n'avez pas les permission.")
            return

        # compare cooldown time.
        isCooldownValid = (datetime.datetime.now() - ShootOut.lastTimeCalled).total_seconds() > ShootOut.cooldown

        # is cooldown unvalid, error.
        if(not isCooldownValid):
            await message.channel.send("un so à déja été créé récement.")
            return

        # update time for next cooldown.
        ShootOut.lastTimeCalled = datetime.datetime.now()

        # get param (pseudo viewer to shootout).
        param = self.extractParams(message, isSplitBySpace=False)
        if param.startswith("@"):
            param = param[1:]

        # get token.
        objToken = client.getTokenObj()

        # get users.
        users = await client.fetch_users(
            names=[param], 
            token=objToken["bot"]["appAccessToken"], 
            force=False
        )

        # verify if user is found.
        if len(users) == 0:
            await message.channel.send("pseudo inconnu.")
            return

        await client.shootOut(users[0].id)
        