import json, os
from elements import wall as w, platform as plat
def getPalette() -> dict: return json.loads(open(os.path.join(os.path.dirname(__file__), 'palette.json')).read())
def getMap() -> dict:
    palette = getPalette()
    rawmap = json.loads(open(os.path.join(os.path.dirname(__file__), '../maps/map.json')).read())
    finalWallList = [w.Wall(wall[0], wall[1], wall[2], wall[3], palette[wall[4]], False) for wall in rawmap['wall']]
    finalPlatList = [plat.Platform(platform[0], platform[1], platform[2], platform[3], palette[platform[4]]) for platform in rawmap['platform']]
    return finalWallList, finalPlatList
