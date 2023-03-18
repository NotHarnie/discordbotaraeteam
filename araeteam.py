import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name="Created by Harnie#8306"))
    while True:
        for guild in bot.guilds:
            for member in guild.members:
                participant_role = discord.utils.get(member.guild.roles, name="Participant")
                if participant_role in member.roles:
                    team_roles = ["Forgeron", "Mage", "Épéiste", "Invocateur", "Alchimiste", "Archer", "Assassin", "Prêtre(sse)"]
                    member_roles = [role.name for role in member.roles if role.name in team_roles]
                    if not member_roles:
                        role = random.choice(team_roles)
                        new_role = discord.utils.get(member.guild.roles, name=role)
                        print(f'Adding role {role} to {member}.')
                        if new_role is not None:
                            await member.add_roles(new_role)
                            print(f'Role added to {member}.')
                        else:
                            print(f'Error: role {role} not found.')
                    else:
                        print(f'Skipping {member} - already has a team role.')
                else:
                    team_roles = ["Forgeron", "Mage", "Épéiste", "Invocateur", "Alchimiste", "Archer", "Assassin", "Prêtre(sse)"]
                    member_roles = [role.name for role in member.roles if role.name in team_roles]
                    if member_roles:
                        for role_name in member_roles:
                            role = discord.utils.get(member.guild.roles, name=role_name)
                            print(f'Removing role {role_name} from {member}.')
                            await member.remove_roles(role)
                            print(f'Role removed from {member}.')
        await asyncio.sleep(5)

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    participant_role = discord.utils.get(member.guild.roles, name="Participant")
    if participant_role in member.roles:
        team_roles = ["Forgeron", "Mage", "Épéiste", "Invocateur", "Alchimiste", "Archer", "Assassin", "Prêtre(sse)"]
        role = random.choice(team_roles)
        new_role = discord.utils.get(member.guild.roles, name=role)
        print(f'Adding role {role} to {member}.')
        if new_role is not None:
            await member.add_roles(new_role)
            print(f'Role added to {member}.')
        else:
            print(f'Error: role {role} not found.')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')

bot.description = "Bot créé par Harnie#8306. Ce bot donne aléatoirement un rôle à un membre s'il est membre du rôle \"Participant\" et n'a pas encore de rôle d'équipe. Si le rôle \"Participant\" est enlevé, les rôles d'équipe seront également enlevés."

bot.run('token')