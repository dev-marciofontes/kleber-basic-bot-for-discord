"""
Aplicação de um Bot do discord simples
"""

import random
import jokes
import requests
import lightbulb
import string


bot = lightbulb.BotApp(
    token=open("tokens/token_ds.txt", "r").read(),
    default_enabled_guilds=int(open("tokens/ds_channel_id.txt", "r").read()),
)


# Saudação
@bot.command
@lightbulb.command("msg_kleber", "Saudação amigos do Kleber")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context) -> None:
    await ctx.respond("*Olá, CMF! Eu sou o Kleber!*")


# Piadas
piadas = jokes.get_piadas()


@bot.command
@lightbulb.command("piada", "Receba uma piada")
@lightbulb.implements(lightbulb.SlashCommand)
async def piada(ctx: lightbulb.Context) -> None:
    numero_piada = random.randint(1, len(piadas))
    await ctx.respond(f"*{piadas[numero_piada]}*")


# Calculadora
@bot.command
@lightbulb.command("calculadora", "Calculadora")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calculadora(ctx: lightbulb.Context) -> None:
    pass


@calculadora.child
@lightbulb.option("n2", "Segundo número", type=float)
@lightbulb.option("n1", "Primeiro número", type=float)
@lightbulb.command("soma", "Operação de adição")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx: lightbulb.Context):
    result = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f"{ctx.options.n1} + {ctx.options.n2} = **{result}**")


@calculadora.child
@lightbulb.option("n2", "Segundo número", type=float)
@lightbulb.option("n1", "Primeiro número", type=float)
@lightbulb.command("subtração", "Operação de subtração")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subtração(ctx: lightbulb.Context):
    result = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f"{ctx.options.n1} - {ctx.options.n2} = **{result}**")


@calculadora.child
@lightbulb.option("n2", "Segundo número", type=float)
@lightbulb.option("n1", "Primeiro número", type=float)
@lightbulb.command("multiplicação", "Operação de multiplicação")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplicação(ctx: lightbulb.Context):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f"{ctx.options.n1} * {ctx.options.n2} = **{r}**")


@calculadora.child
@lightbulb.option("n2", "Segundo número", type=float)
@lightbulb.option("n1", "Primeiro número", type=float)
@lightbulb.command("divisão", "Operação de divisão")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divisão(ctx: lightbulb.Context):
    result = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f"{ctx.options.n1} / {ctx.options.n2} = **{result}**")


# Temperatura
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("tokens/api_weather_key.txt", "r").read()


def kelvin_to_celsius(kelvin: float) -> float:
    celsius = kelvin - 273.15
    return celsius


@bot.command
@lightbulb.option("pais", "País", type=str)
@lightbulb.option("cidade", "Cidade", type=str)
@lightbulb.command(
    "temperatura",
    "Informe uma cidade e seu país para saber as condições climáticas atuais!",
)
@lightbulb.implements(lightbulb.SlashCommand)
async def temperatura(ctx: lightbulb.Context) -> None:
    country = ctx.options.pais
    CITY = string.capwords(ctx.options.cidade) + "," + country[0:2].lower()
    url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
    response = requests.get(url).json()

    try:
        temp_kelvin = response["main"]["temp"]
        temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))

        umidade = response["main"]["humidity"]
        vento = response["wind"]["speed"]

        await ctx.respond(
            f"A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius}°C"
            + f"e a umidade é de {umidade}% e o vento é de {vento} m/s."
        )
    except KeyError:
        await ctx.respond(
            "Não foi possível obter informações de temperatura para esta localização."
        )


bot.run()
