import datetime
import aiohttp
import asyncio

class Prismalytics:
    def __init__(self, key, client, save_server=True):
        """
        key: api token for prismalytics
        save_server: option to save server data
        client: discordpy client
        commands: commands that will be recorded by the lib
        servers: server data in which bot is used
        """
        self.key = key
        self.save_server = save_server
        self.client = client
        self.commands = {}
        self.servers = []
        self.time = None

    def process_data(self, message, server):
        # processes data from discord into `servers` and `commands`

        message = message.content.split(" ")[0]
        if message in self.commands.keys():
            self.commands[message] += 1
        else:
            self.commands[message] = 1
        
        if self.save_server:
            match = next((i for i in self.servers if i["name"] == server.name), None)
            
            if match is None:
                new_server = {
                    "name": server.name,
                    "member_count": server.member_count,
                    "region": server.region,
                    "bot_messages": 1
                    }
                self.servers.append(new_server)

            else:
                match["bot_messages"] += 1
            
    async def send(self, ctx):
        """
        processes data and sends every 2 minutes
        TODO: refactor so that users don't need to use ctx
        """
        unset = False
        if self.time is None:
            self.time = datetime.datetime.now()
            unset = True

        server = ctx.message.guild
        self.process_data(ctx.message, server)
        

        curr_time = datetime.datetime.now()
        interval = (curr_time - self.time).total_seconds() / 60
        if (unset or interval > 2):
            self.time = curr_time
            data = {
                "commands":  self.commands,
                "save_server": self.save_server
                }
            if self.save_server: 
                data["servers"] = self.servers

            # refactor this to use asyncio requests and have the program run in the background
            async with aiohttp.ClientSession() as session:
                await session.post("https://prismalytics.herokuapp.com/send_data", json=data, headers={'key': self.key})

            # reinitialize stored data as it has been sent
            self.commands = {}
            self.servers = []