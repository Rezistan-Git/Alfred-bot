import discord
from discord.ext import commands

# Activer les intents pour détecter les nouveaux membres
intents = discord.Intents.default()
intents.members = True  # Active l'événement on_member_join
intents.message_content = True

# Créer une instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Remplace par l'ID du canal de bienvenue sur ton serveur
WELCOME_CHANNEL_ID = 1344342386695868485  # Mets ici l'ID de ton canal

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté et prêt !')

@bot.event
async def on_member_join(member):
    # 1️⃣ Envoi du message de bienvenue dans le serveur
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"🎉 Bienvenue {member.mention} sur le serveur Albilab ! Nous sommes ravis de t'accueillir !")

    # 2️⃣ Envoi d'un message privé avec un fichier joint
    try:
        dm_message = (
            f"Salut {member.mention} !  Bienvenue sur le serveur Discord d'Albilab !\n\n"
    "Nous sommes ravis de t’accueillir dans notre communauté !\n"
    "Le FabLab est un espace collaboratif où tu peux concevoir, fabriquer, apprendre et partager autour de projets innovants.\n\n"
    "📘 Tu trouveras ci-joint notre **livret d’accueil**, qui contient toutes les informations importantes :\n"
    "Les horaires, les dates des initiations à venir, les tarifs, les contacts utiles, et bien plus encore.\n"
    "N’hésites pas à nous poser des questions ou à te présenter sur le serveur !\n\n"
    "**💡Pour mieux te connaître** et t'orienter nous t'invitons à remplir ce formulaire : https://tinyurl.com/FormulaireAccueilAlbilab\n\n"
    "**💡Pour adhérer à l'association**, tu peux nous rejoindre via ce lien : https://tinyurl.com/AdhesionAlbilab2025\n"
    "L'adhésion à l'association te permettra d'acccéder à toutes les ressources du Discord\n\n"
    "Encore bienvenue parmi nous !"
        )
        file_path = "Livret d'accueil.pdf"  # Remplace par ton fichier (PDF, image, etc.)
        
        # Envoi du message privé avec un fichier joint
        await member.send(dm_message, file=discord.File(file_path))
        print(f"Message privé envoyé à {member.name}.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message privé à {member.name}: {e}")

# Liste des codes d'adhésion valides
valid_codes = {
    "ABC123": False,
    "XYZ789": False,
    # etc...
}
        
@bot.command()
async def code(ctx, entered_code):
    if isinstance(ctx.channel, discord.DMChannel):  # Vérifie que c’est en message privé
        guild = discord.utils.get(bot.guilds, name="NOM_DU_SERVEUR")
        member = guild.get_member(ctx.author.id)
        role = discord.utils.get(guild.roles, name="Adhérent")

        if entered_code in valid_codes and not valid_codes[entered_code]:
            await member.add_roles(role)
            valid_codes[entered_code] = True
            await ctx.send("✅ Code accepté, rôle attribué !")
        else:
            await ctx.send("❌ Code invalide ou déjà utilisé.")
    else:
        await ctx.send("Merci d’envoyer votre code en message privé.")

# Démarrer le bot (Remplace 'TON_TOKEN' par ton vrai token)
import os
TOKEN = os.environ["DISCORD_TOKEN"]
bot.run(TOKEN)
