from telethon import events
from config import bot
import logging
import docker_controler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARN)

@bot.on(events.NewMessage(pattern="/start"))
async def _(event):
    await bot.send_message(event.chat_id, "I am God!!!!")


@bot.on(events.NewMessage(pattern="/create"))
async def _(event):
    r = await event.get_reply_message()    
    if r == None:
        await event.reply("Usage:\n`/create <repo link> <bot username>`\n\n Reply to ENV vars")
        return
    
    env = r.raw_text.strip()
    env = env.replace('"', '\\"')
    try:
        _, git_link, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/create <repo link> <bot username>`\n\n Reply to ENV vars")
        return
    
    o = await docker_controler.create(git_link, name, env)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/restart"))
async def _(event):
    try:
        _, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/restart <bot username>`")
    o = await docker_controler.restart(name)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/remove"))
async def _(event):
    try:
        _, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/remove <bot username>`")
    o = await docker_controler.remove(name)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/sstart"))
async def _(event):
    try:
        _, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/start <bot username>`")
    o = await docker_controler.start(name)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/stop"))
async def _(event):
    try:
        _, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/stop <bot username>`")
    o = await docker_controler.stop(name)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/update"))
async def _(event):
    try:
        _, name = event.raw_text.split()
        name = name.replace("@", "").lower()
    except:
        await event.reply("Usage:\n`/update <bot username>`")
    o = await docker_controler.update(name)
    await event.reply(f"```Logs\n{o}```")


@bot.on(events.NewMessage(pattern="/status"))
async def _(event):
    containers = docker_controler.get_containers()
    res = ""
    for c in containers:
        res += f"@{c.get('name')} {c.get('status')}\n"

    await event.reply(res)



bot.start()

bot.run_until_disconnected()
