# Prisma.py

Simple wrapper for Prismanalytics Discord bot analytics that interfaces with `discord.py`. 

## Setup
Initialize the connection with our library like this:

```python
import prismapy

client = discord.Client()
analytics = prismapy.Prismalytics("<api key>", client)
```

And then, add this code to your `discordpy` bot's code:

```python
@client.event
async def on_command(ctx):
    analytics.send(ctx)
```

This will send the data to our api through the library and you'll have a beatiful dashboard like this:

![demo](https://github.com/Uzay-G/prisma.py/blob/master/galena2.gif)