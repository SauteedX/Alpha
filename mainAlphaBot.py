import discord

discord_token = '1042427195051737128'
client = discord.Client
client.run(token = discord_token,)

class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("Standby...")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")
       

    
import asyncio

async def on_message(message):
    if message.content.startswith("!청소 "):
        purge_number = message.content.replace("!청소 ", "")
        check_purge_number = purge_number.isdigit()
        if check_purge_number == True:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했습니다.")
            await asyncio.sleep(5)
            await msg.delete()

        else:
            await message.channel.send("올바른 값을 입력해주세요.")
