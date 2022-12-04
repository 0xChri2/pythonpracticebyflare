import datetime
import discord
from discord.ext import commands
import requests
import json
import asyncio

# Erstelle eine Liste von Discord-Intents, die der Bot verwenden soll
intents = discord.Intents.default()
intents.members = True

# Erstelle den Bot und übergebe die Liste der Discord-Intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Hole die ID des angegebenen Discord-Kanals
    channel_id = bot.get_channel(CHANNEl_ID)

    # Poste eine Willkommensnachricht im Discord-Kanal
    await channel_id.send('Ich bin der Commit-Bot und werde über neue Commits im ESPHSNR2022-23 Repository benachrichtigen.')
    last_commit_id = None
    # Sende in regelmäßigen Abständen Anfragen an das Repository-API
    while True:
        # Sende eine Anfrage an 'https://api.github.com/repos/ImChri2/ESPHSNR2022-23/commits' mit user id und token
        response = requests.get('https://api.github.com/repos/ImChri2/ESPHSNR2022-23/commits', auth=('Username', 'Github Token'))

        # Parse die Antwort als JSON-Dokument
        data = json.loads(response.text)

        # Überprüfe, ob es neue Commits im Repository gibt
        if data[0]['sha'] != last_commit_id:
            # Speichere die ID des neuesten Commits
            last_commit_id = data[0]['sha']

            # Erstelle eine Nachricht mit den Informationen zu den neuesten Commits
            message = "Neuester Commit:\n"
            commit = data[0]
            commit_url = f"https://github.com/ImChri2/ESPHSNR2022-23/commit/{commit['sha']}"

            # Erstelle das Embed-Objekt
            embed = discord.Embed(
                title=f"Neuer Commit: {last_commit_id[:7]}",
                url=data[0]['html_url'],
                description=data[0]['commit']['message'].split("\n\n")[0],
                color=0x30d6f8,
                timestamp=datetime.datetime.strptime(data[0]['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
            )

            # Setze die Eigenschaften des Embed-Objekts
            embed.set_author(name="Commit Announcer", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
            if len(data[0]['commit']['message'].split("\n\n")) > 1:
                embed.add_field(name="Beschreibung:", value=data[0]['commit']['message'].split("\n\n")[1], inline=True)
            #embed.add_field(name="Branch", value=data[0]['commit']['branch'], inline=True)
            embed.add_field(name="Hash", value=data[0]['sha'][:7], inline=True)
            embed.set_footer(text=f"Commited by { data[0]['commit']['author']['name'] }", icon_url=data[0]['author']['avatar_url'])


            # Sende die Embedded Message im Discord-Kanal
            await channel_id.send(embed=embed)

            # Warte eine bestimmte Zeit, bevor die nächste Anfrage gesendet wird
            await asyncio.sleep(60)
bot.run('Bot Token')