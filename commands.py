import io
import sys
import os
import discord
import random
import subprocess



class Commands(discord.Client):

    """
    def dc(expression):
        dcFilepath = "C:\\Program Files (x86)\\GnuWin32\\bin"
        tempdcFilepath = os.getcwd()+"\\tempdc.txt"
        expression = '"'+expression+'"'
        dcFilepath = '"'+dcFilepath+"\\dc.exe"+'"'+" -e "
        command = '"'+dcFilepath+expression+" > "+'"'+tempdcFilepath+'"'+'"'
        command = os.path.normcase(command)
        print(command)
        os.system(command)
        f = open(tempdcFilepath, "r")
        output = f.read()
        f.close()
        os.remove(tempdcFilepath)
        return output
    """
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.multiLineCode = 0
        self.multiLineChannels = []

    def isAdmin(self, message):
            print("User "+str(message.author.id)+" is trying to acces admin functions")
            if message.author.id == 316270897638146059:
                print("Admin command executed")
                return 1
            return 0


    async def spam(client, message, text):
            output = text[1]
            for x in range(int(text[2])):
                #output = output + "\n" + text[1]
                await message.channel.send(output)
            return

    async def a(client, message, text):
        print("a")
        return

    async def meowwoem(client, message, text):
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689123594341/image0-5-2.gif")
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689421258912/image0-3-1.gif")
        return

    async def mock(client, message, text):
        output = ''.join(random.choice((str.upper, str.lower))(c) for c in text[1])
        await message.channel.send(output)
        return


    async def restart(client, message, text):
        command = sys.executable +" "+ '"'+os.path.join(os.getcwd(), "main.py"+'"')
        print(command)
        await message.channel.send("Restarting...\n```"+command+"```")
        await message.channel.send("https://c.tenor.com/2kYfZmX6v6UAAAAC/stairs-da.gif")
        os.system(command)
        sys.exit("Process restarting")

    async def discordpy(client, message, text):
        if client.isAdmin(message):
            client.multiLineCode = client.multiLineCode + 1
            thisChannel = [message.channel, "discordpyint"]
            client.multiLineChannels.append(thisChannel)
            print("Starting discordpy environment")
            await message.channel.send("Starting discordpy environment")
            return
        await message.channel.send("Higher permissions required")
        return

    async def discordpyint(client, message, text):
        if client.isAdmin(message):
            if message.content == "exit":
                client.multiLineCode = client.multiLineCode - 1
                for x in range(len(client.multiLineChannels)):
                    thisChannel = client.multiLineChannels[x]
                    if thisChannel[1] == "discordpyint":
                        client.multiLineChannels.pop(x)
                        print("Closed discordpy environment")
                        await message.channel.send("Closed discordpy environment")
            
            stdout = subprocess.Popen(message.content, shell=True, stdout=subprocess.PIPE).stdout
            output = stdout.read().decode("utf-8").strip("'b")
            output = "```\n"+output+"\n```"
            print(output)
            await message.channel.send(output)
            return
        await message.channel.send("Higher permissions required")
        return