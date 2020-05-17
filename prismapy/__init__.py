import datetime
import json
import requests

class Prismalytics:
    def __init__(self, key, client, save_server=True):
        self.key = key
        self.save_server = save_server
        self.client = client
        self.commands = {}
        self.servers = []
        self.time = None


    def send(self, ctx):
        unset = False
        if self.time is None:
            self.time = datetime.datetime.now()
            unset = True

        message = ctx.message.content.split(" ")[0]
        server = ctx.message.guild
        if message in self.commands.keys():
            self.commands[message] += 1
        else:
            self.commands[message] = 1
        
        if self.save_server:
            match = next((i for i in self.servers if i["name"] == server.name), None)
            
            if match is None:
                self.servers.append({"name": server.name, "member_count": server.member_count, "region": server.region, "bot_messages": 1})
            else:
                match["bot_messages"] += 1

        curr_time = datetime.datetime.now()
        if (unset or ((curr_time - self.time).total_seconds() / 60) > 2):
            self.time = curr_time
            if self.save_server:
                data = {'commands': json.dumps(self.commands), 'servers': json.dumps(self.servers), 'save_server': True}
            else: data = {'commands': json.dumps(self.commands), 'save_server': False}
            requests.post('https://prismalytics.herokuapp.com//send_data', data=data, headers={'key': self.key})
            self.commands = {}
            self.servers = []