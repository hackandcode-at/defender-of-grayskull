import discord
from discord import app_commands
from discord.ext import commands

# Intents für den Bot einstellen
intents = discord.Intents.default()

# Erstelle die Bot-Klasse
class DefenderOfGrayskull(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        # Zeige im Terminal an, wenn der Bot startklar ist
        print(f"{self.user} ist online und bereit, Grayskull zu verteidigen!")
        
        # Synchronisiere die Slash Commands mit Discord
        await self.tree.sync()
        print("Slash Commands synchronisiert.")

# Erstelle den Bot
bot = DefenderOfGrayskull()

# Slash Command Beispiel
@bot.tree.command(name="grayskull", description="Beschwöre die Macht von Grayskull!")
async def grayskull(interaction: discord.Interaction):
    await interaction.response.send_message("Bei der Macht von Grayskull! 💪✨")

# Starte den Bot
bot.run('DEIN_DISCORD_BOT_TOKEN')
