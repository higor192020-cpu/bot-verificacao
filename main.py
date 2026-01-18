import discord
from discord.ext import commands

# Intents completos (evita erro no Replit)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

ID_CARGO = 1462554681070059694

class Verificacao(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✅ Verificar", style=discord.ButtonStyle.success)
    async def verificar(self, interaction: discord.Interaction, button: discord.ui.Button):
        cargo = interaction.guild.get_role(ID_CARGO)

        if cargo is None:
            await interaction.response.send_message(
                "❌ Cargo não encontrado. Avise um administrador.",
                ephemeral=True
            )
            return

        if cargo in interaction.user.roles:
            await interaction.response.send_message(
                "Você já está verificado.",
                ephemeral=True
            )
            return

        await interaction.user.add_roles(cargo)
        await interaction.response.send_message(
            "✅ Verificação concluída! Cargo liberado.",
            ephemeral=True
        )

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")
    try:
        bot.add_view(Verificacao())
    except:
        pass

@bot.command()
async def setup(ctx):
    embed = discord.Embed(
        title="🔐 Verificação",
        description="Clique no botão abaixo para se verificar e acessar o servidor.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed, view=Verificacao())

bot.run("TOKEN")
