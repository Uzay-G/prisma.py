# Prisma.py

Simple wrapper for Prismanalytics Discord bot analytics that interfaces with `discord.py`. 

## Setup

Install prismalytics with `pip`:

```python
pip install prismapy
```

- Create an account / login at https://prismalytics.herokuapp.com and register a new bot.
- Copy it's token

- Initialize the connection with our library like this:

```python
import prismapy

client = discord.Client()
analytics = prismapy.Prismalytics("<bot api key>", client)
```

- And then, add this code to your `discordpy` bot's code:

```python
@client.event
async def on_command(ctx):
    await analytics.send(ctx)
```

This will send the data to our api through the library and you'll have a beatiful dashboard like this:

![demo](https://github.com/Uzay-G/prisma.py/blob/master/galena2.gif)

## TODO

- Modularise code to support without ctx
- Allow more flexibility in the way data is processed
- Make the recurrent api calls run in the background instead of calling them when a new message is received.
