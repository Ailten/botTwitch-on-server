from classFolder.TwitchBot import TwitchBot
import os

bot = TwitchBot()
bot.run()

# mark process for kill easilly.
pathPid = f"{bot.pathFolder}/main.pid"
if os.path.isfile(pathPid)
    with open(pathPid, "w") as f:
        f.write(str(os.getpid()))

# execute in background.
# nohup python3 <path>/mon_script.py &

# kill the background execution.
# kill $(cat <path>/main.pid)