from classFolder.TwitchBot import TwitchBot
import os

bot = TwitchBot()
bot.run()

# mark process for kill easilly.
with open(f"{bot.pathFolder}/main.pid", "w") as f:
    f.write(str(os.getpid()))

# execute in background.
# nohup python3 <path>/mon_script.py &

# kill the background execution.
# kill $(cat <path>/main.pid)