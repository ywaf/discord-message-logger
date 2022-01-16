# Made By Leho | github.com/lehoooo | leho.dev
import discord
from discord.ext import commands
import sys
import json
import os
from os.path import exists

print("Starting")

bot = commands.Bot(command_prefix='>')
try:
    with open("config.json", "r") as configfile:
        config = json.load(configfile)

except Exception as e:
    print("Error Loading Config " + str(e))
    sys.exit(9)


TOKEN = str(config['token'])

if not os.path.isdir(os.getcwd() + "/logs"):
    os.mkdir(os.getcwd() + "/logs")
    print("made logs folder")


@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "#" + bot.user.discriminator)
    print("Ready")


def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["messages"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

@bot.event
async def on_message(message):
    serverid = str(message.guild.id)
    channelid = str(message.channel.id)
    author = str(message.author)
    content = str(message.content)
    userid = str(message.author.id)
    # messageid = str(message.id)
    time = str(message.created_at)
    channel = str(message.channel)
    print(author, userid, content, time)
    folderpath = os.getcwd() + """/logs/""" + str(serverid) + " - " + str(message.guild)
    path = folderpath + """/""" + str(channelid) + " - " + str(channel) + ".json"


    if exists(str(path)):
        print("file exists")

    else:
        if not os.path.isdir(folderpath):
            os.mkdir(folderpath)
            print("made folder")

        print("making json now")
        makejson = open(path, "w")
        makejson.write("""{
    "messages": [
    ]
}
        """)
        makejson.close()
        print("made file, writing content now")

    towrite = {
        "Username": "" + str(author) + "",
        "Userid": "" + str(userid) + "",
        "Content": "" + str(content) + "",
        "Time": "" + str(time) + ""
    }

    write_json(towrite, path)



bot.run(TOKEN)

