import datetime
import json

class Prismalytics:
    def __init__(self, key, client, save_server=True):
        self.key = key
        self.save_server = save_server
        self.client = client
        self.commands = {}
        self.servers = []


    def send(message):
        unset = False
        try:
            self.time
        except NameError:
            self.time = datetime.datetime.now()
            unset = True

        message = ctx.message.content.split(" ")[0]
        server = ctx.message.guild
        if message in commands.keys():
            commands[message] += 1
        else:
            commands[message] = 1
        
        if save_server:
            match = next((i for i in servers if i["name"] == server.name))
            
            if match is None:
                servers.append({name: server.name, member_count: server.member_count, region: server.region, bot_messages: 1})
            else:
                match["bot_messages"] += 1

        curr_time = datetime.datetime.now()
        if (unset or ((self.time - curr_time).total_seconds() / 60) > 2):
            self.time = curr_time
            guild = message.guild
            if save_server:
                data = {'commands': json.dumps(self.commands), 'servers': json.dumps(self.servers)}
            else data = {'commands': json.dumps(self.commands), 'save_server': False}
            requests.post('https://prismalytics.herokuapp.com/send_data', data=data, headers={'key': self.key})
