from twitchio.ext import commands, eventsub
from classFolder.Json import Json
from classFolder.Http import Http
import re
import datetime
import json

# importe commandes.
from classFolder.commandes.Hello import Hello
from classFolder.commandes.Clip import Clip
from classFolder.commandes.ShootOut import ShootOut

# DOC : https://twitchio.dev/en/stable/index.html
# pist for event reward : https://twitchio.dev/en/stable/exts/eventsub.html#twitchio.ext.eventsub.AutoRewardRedeem.reward


class TwitchBot(commands.Bot):
    pathFolder: str
    #botPartialUser: twitchio.PartialUser
    #brodcasterPartialUser: twitchio.PartialUser
    #esbot
    #esclient


    # contructor.
    def __init__(self):

        # set path.
        self.pathFolder = "home/faouzi/Documents/myBotTwitchPython"
        self.pathToken = f"/{self.pathFolder}/json/tokenTwitch.json"

        # get token obj.
        objToken = self.getTokenObj()

        # regen access token.
        isAccessTokenValid = (int(datetime.datetime.now().timestamp()) - objToken["bot"]["appAccessTokenGenerateDate"]) > objToken["bot"]["appAccessTokenExpiresIn"]
        if(isAccessTokenValid):
            await self.refreshAccessToken()

        ## set esbot and esclient.
        #self.esbot = commands.Bot.from_client_credentials(
        #    client_id = objToken["bot"]["idClient"],
        #    client_secret = objToken["bot"]["secretClient"]
        #)
        #self.esclient = eventsub.EventSubClient(
        #    self.esbot,
        #    webhook_secret = '...', # TODO.
        #    callback_route = 'https://your-url.here/callback' # TODO.
        #)
        #
        # set event esbot.
        #@self.esbot.event()
        #async def event_eventsub_notification_followV2(payload) -> None:
        #    print('Received event!')
        #    print(f'{payload.data.user.name} followed woohoo!')

        # init the bot.
        super().__init__(
            nick = objToken["bot"]["pseudo"],
            token = objToken["bot"]["userAccessToken"],
            initial_channels = [objToken["brodcaster"]["pseudo"]],
            prefix = ""
        )

        # create partial users.
        self.botPartialUser = self.create_user(
            user_id = objToken["bot"]["id"], 
            user_name = objToken["bot"]["pseudo"]
        )
        self.brodcasterPartialUser = self.create_user(
            user_id = objToken["brodcaster"]["id"], 
            user_name = objToken["brodcaster"]["pseudo"]
        )

        # all commandes set to the bot.
        self.commandes = [
            Hello(),
            Clip(),
            ShootOut()
        ]

        # loop for webhook custom.
        #self.loop.run_until_complete(self.__ainit__())

    
    # function ainit.
    #async def __ainit__(self) -> None:
    #
    #    self.loop.create_task(self.esclient.listen(port=4000))
    #
    #    objToken = self.getTokenObj()
    #
    #    try:
    #        await self.esclient.subscribe_channel_follows_v2(
    #            broadcaster = objToken["brodcaster"]["id"], 
    #            moderator = objToken["bot"]["id"]
    #        )
    #    except:
    #        print("error in ainit")
    #        pass


    # event when bot is conected to channel.
    async def event_ready(self):

        print(f"[{self.nick}] is ready !")


    # event when viewer join the chat.
    async def event_join(self, channel, user):

        print(f"viewer [{user.name}] joint the chat !")


    # event when a message is catch on chat.
    async def event_message(self, message):

        if(message.echo): # skip message from self.
            return

        #print(f"{message.author.name}: {message.content}") # warning : name can be None.
        #print(f"id user : {message.author.id}")

        for command in self.commandes: # loop on every commandes.
            if(re.search(command.regex, message.content)):
                await command.execute(self, message)


    # function return object json token.
    def getTokenObj(self):
        return Json.read(self.pathToken)


    # function save the object json token.
    def setTokenObj(self, objToken):
        return Json.write(self.pathToken, objToken)


    # function to make a shoutout.
    async def shoutOut(self, broadcasterId):

        objToken = self.getTokenObj()

        await self.botUser.shoutout(
            token = objToken["bot"]["appAccessToken"],
            to_broadcaster_id = broadcasterId, 
            moderator_id = objToken["bot"]["id"]
        )


    # function to make a clip.
    async def clip(self):

        objToken = self.getTokenObj()

        await self.botUser.create_clip(
            token = objToken["bot"]["appAccessToken"],
            to_broadcaster_id = False
        )

    
    # refresh token and save in file json.
    async def refreshAccessToken(self):

        objToken = self.getTokenObj()

        #TODO: ask for the other token (do not implement befor need to be) in other function.
        #objToken["bot"]["userAccessToken"] = ""
        #objToken["bot"]["userAccessTokenExpiresIn"] = ""

        try: # last update : 16/05/2025 -> explire in 2 month.
            newAccessToken = await Http.askForNewAccessToken(objToken)
            objToken["bot"]["appAccessToken"] = newAccessToken["access_token"]
            objToken["bot"]["appAccessTokenExpiresIn"] = newAccessToken["expires_in"]
            objToken["bot"]["appAccessTokenGenerateDate"] = int(datetime.datetime.now().timestamp())
        except:
            return

        self.setTokenObj(objToken)



#    # debug.
#    async def event_channel_join_failure(self, channel):
#        print("- [debug event] event_channel_join_failure ->")
#        print(channel)
#    async def event_channel_joined(self, channel):
#        print("- [debug event] event_channel_joined")
#        print(channel)
#    async def event_error(self, error, data):
#        print("- [debug event] event_error ->")
#        print(error)
#        print(data)
#    async def event_join(self, channel, user):
#        print("- [debug event] event_join ->")
#        print(channel)
#        print(user)
#    #async def event_message(self, message):
#    #    print("- [debug event] event_message ->")
#    #    print(message)
#    async def event_mode(self, channel, user, status):
#        print("- [debug event] event_mode ->")
#        print(channel)
#        print(user)
#        print(status)
#    async def event_notice(self, message, msg_id, channel):
#        print("- [debug event] event_notice ->")
#        print(message)
#        print(msg_id)
#        print(channel)
#    async def event_part(self, user):
#        print("- [debug event] event_part ->")
#        print(user)
#    async def event_raw_data(self, data):
#        print("- [debug event] event_raw_data ->")
#        print(data)
#    async def event_raw_notice(self, data):
#        print("- [debug event] event_raw_notice ->")
#        print(data)
#    async def event_raw_usernotice(self, channel, tags):
#        print("- [debug event] event_raw_usernotice ->")
#        print(channel)
#        print(tags)
#    #async def event_ready(self):
#    #    print("- [debug event] event_ready ->")
#    async def event_reconnect(self):
#        print("- [debug event] event_reconnect ->")
#    async def event_token_expired(self):
#        print("- [debug event] event_token_expired ->")
#    async def event_usernotice_subscription(self, metadata):
#        print("- [debug event] event_usernotice_subscription ->")
#        print(metadata)
#    async def event_userstate(self, user):
#        print("- [debug event] event_userstate ->")
#        print(user)


