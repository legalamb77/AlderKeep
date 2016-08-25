from sys import exit
from random import randint

class Scene(object):
    def __init__(self,player_stats):
        self.player_stats=player_stats

    def enter(self):
        print "You have found an unfinished scene. Woops."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map=scene_map

    def play(self):
        #Get player name, boon, and bane
        stats = {
                "name":"Aerith",
                "HEALTH":10,
                "STRENGTH":10,
                "SMARTS":10,
                "SPEED":10,
                "DEFENSE":10
                }
        print "Hero, you alone have the courage to save this land. What is your name?"
        name = raw_input(">>")
        stats["name"]=name
        print "Your mother was in the ROYAL GUARD, and she always said heroes had five main traits, HEALTH, STRENGTH, SMARTS, SPEED, and DEFENSE."
        print "Which of these are you best at?"
        boon = raw_input(">>")
        while boon!="HEALTH" and boon!="STRENGTH" and boon!="SMARTS" and boon!= "SPEED" and boon !="DEFENSE":
            print "Take this seriously, young hero."
            boon = raw_input(">>")
        stats[boon]=18
        print "Which of them did you really suck at?"
        bane = raw_input(">>")
        while bane!="HEALTH" and bane!="STRENGTH" and bane!="SMARTS" and bane!="SPEED" and bane!="DEFENSE":
            print "Take this seriously, young hero."
            bane = raw_input(">>")
            if bane=="YOUAREABIGGUY":
                print "FOR YOU"
                #set health and strength to 20
                stats["HEALTH"]=20
                stats["STRENGTH"]=20
        stats[bane]=5
        print "Well then, let us begin."
        #Run first scene
        current_scene=self.scene_map.opening_scene
        last_scene=self.scene_map.next_scene('fin')
        while current_scene!=last_scene:
            #current_scene.enter() needs to return the name of the next scene
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    def enter(self):
        print "You have died an ignoble death, the land shall be terrorized forevermore."
        exit(1)

class Drawbridge(Scene):

    def enter(self):
        print "The rain batters down on your mother's armor as you are confronted with the sprawling home of the LICH KING, known only as ALDER KEEP."
        print "The drawbridge is raised, and the moat churns with dark shapes in the water. Lurid light pours from several small windows about the walls of the keep."
        print "The grass is slick with mud underfoot, and the road you came in on is but a dirt path. A number of trees line the edges of the moat."
        print "What dost thou do?"
        act=raw_input(">>")
class Grand_Hall(Scene):

    def enter(self):
        pass

class Pantry(Scene):

    def enter(self):
        pass

class Armory(Scene):

    def enter(self):
        pass

class Dungeon(Scene):

    def enter(self):
        pass

class Throne_Room(Scene):

    def enter(self):
        pass

    def battle(self):
        pass

class Map(object):

    sceneList={
            'Drawbridge':Drawbridge(),
            'Death':Death(),
            'Grand Hall':Grand_Hall(),
            'Pantry':Pantry(),
            'Armory':Armory(),
            'Dungeon':Dungon(),
            'Throne_Room':Throne_Room(),
            }

    def __init__(self, start_scene):
        #Sets the first scene to the parameter which Map is called with
        self.start_scene=start_scene

    def next_scene(self, scene_name):
        #Retrieve and return the function(or result of said function?) based off the scene name returned by
        #the ending of the current scene
        return Map.sceneList.get(scene_name)

    def opening_scene(self):
        #return the starting scene that was given to the map as a parameter
        return self.next_scene(self.start_scene)

a_map=Map('Drawbridge')
a_game=Engine(a_map)
a_game.play()
