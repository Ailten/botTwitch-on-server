import re


class Commande:
    regex: str # name of commande (use to recognise, and use to call).
    

    # the execution of commande.
    async def execute(self, client, message):
        pass

    
    # get params from message.
    def extractParams(self, message, isSplitBySpace=True):

        param = re.sub("^![a-zA-Z]{1,}", "", message.content)

        if(not isSplitBySpace):
            return param

        return param.split(" ")
