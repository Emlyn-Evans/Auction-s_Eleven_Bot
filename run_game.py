from gameEngine import GameEngine, NPCRandomBot
import importlib

# List your bots here
botsToRun = {
    "template_files.examples.randomBidder": 4,
    "template_files.examples.randomAccuser": 1,
    "NPC": 4,
}

engine = GameEngine()

for b in botsToRun:
    for i in range(botsToRun[b]):
        if b == "NPC":
            engine.registerBot(NPCRandomBot(), team="NPC")
        else:
            botClass = importlib.import_module(b)
            engine.registerBot(botClass.CompetitorInstance(), team=b)
engine.runGame()