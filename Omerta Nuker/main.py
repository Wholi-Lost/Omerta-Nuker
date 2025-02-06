import discord
from discord.ext import commands
import asyncio

TOKEN = "Your_bot_token"  
GUILD_ID = 1336944927845781534  
CHANNEL_NAME = "Chanel_name"  
CHANNEL_COUNT = 200  
ROLE_NAME = "Role name"  
ROLE_COUNT = 200  

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Erreur : Guile introuvable. Vérifie l'ID.")
        await bot.close()
        return

    print(f"Guild trouvée : {guild.name} ({guild.id})")
    
    
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer tous les salons de {guild.name} ? (y/n) : ")
    if confirmation.lower() != 'y':
        print("Annulation de la suppression des salons.")
        await bot.close()
        return
    
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Salon {channel.name} supprimé.")
        except discord.Forbidden:
            print(f"Permission insuffisante pour supprimer {channel.name}.")
        except discord.HTTPException as e:
            print(f"Erreur HTTP lors de la suppression du salon {channel.name}: {e}")
    
    print(f"Tous les salons ont été supprimés dans la guilde {guild.name}.")
    
    
    print(f"Création de {CHANNEL_COUNT} nouveaux salons...")
    for i in range(CHANNEL_COUNT):
        try:
            await guild.create_text_channel(CHANNEL_NAME)
            print(f"Salon {i + 1}/{CHANNEL_COUNT} créé.")
        except discord.HTTPException as e:
            print(f"Erreur lors de la création d'un salon: {e}")
    
    print(f"{CHANNEL_COUNT} nouveaux salons ont été créés dans la guilde {guild.name}.")
    
    
    role_confirmation = input(f"Êtes-vous sûr de vouloir créer {ROLE_COUNT} rôles dans {guild.name} ? (y/n) : ")
    if role_confirmation.lower() != 'y':
        print("Annulation de la création des rôles.")
        await bot.close()
        return

    
    print(f"Création de {ROLE_COUNT} rôles...")
    for i in range(ROLE_COUNT):
        try:
            role = await guild.create_role(name=f"{ROLE_NAME} {i + 1}", reason="Création de rôles par le bot")
            print(f"Rôle {role.name} créé.")
        except discord.Forbidden:
            print(f"Permission insuffisante pour créer le rôle.")
        except discord.HTTPException as e:
            print(f"Erreur lors de la création du rôle : {e}")
    
    print(f"{ROLE_COUNT} nouveaux rôles ont été créés dans la guilde {guild.name}.")
    
    
    ban_confirmation = input(f"Êtes-vous sûr de vouloir bannir tous les membres de {guild.name} ? (y/n) : ")
    if ban_confirmation.lower() != 'y':
        print("Annulation du bannissement des membres.")
        await bot.close()
        return

    
    print("Bannissement de tous les membres...")
    for member in guild.members:
        try:
            await member.ban(reason="Bannissement en masse effectué par un bot.")
            print(f"Membre {member.name} banni.")
        except discord.Forbidden:
            print(f"Permission insuffisante pour bannir {member.name}.")
        except discord.HTTPException as e:
            print(f"Erreur lors du bannissement de {member.name}: {e}")
    
    print(f"Tous les membres ont été bannis de la guilde {guild.name}.")
    
    
    await bot.close()

bot.run(TOKEN)
