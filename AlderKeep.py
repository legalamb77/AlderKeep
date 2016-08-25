from sys import exit
from random import randint

class Scene(object):

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
                "DEFENSE":10,
                "SLOT_ONE":"NA",
                "SLOT_TWO":"NA"
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
            #current_scene.enter() needs to return (name of the next scene,stats)
            next_scene_name,new_stats=current_scene.enter(stats)
            stats=new_stats
            current_scene=self.scene_map.next_scene(next_scene_name)
        current_scene.enter(stats)

class Death(Scene):

    def enter(self,ply_sts):
        print "You have died an ignoble death, the land shall be terrorized forevermore."
        exit(1)

class Drawbridge(Scene):

    def enter(self,ply_sts):
        print "The rain batters down on your mother's armor(Unfortunately she left no sword) as you are confronted with the sprawling home of the LICH KING, known only as ALDER KEEP."
        print "The drawbridge is raised, and the moat churns with dark shapes in the water. Lurid light pours from several small windows about the walls of the keep."
        print "The grass is slick with mud underfoot, and the road you came in on is but a dirt path. A number of trees line the edges of the moat."
        print "What dost thou do?"
        while True:
            act=raw_input(">>")
            if act.upper()=="LOOK" or act.upper()=="EXAMINE" or act.upper()=="SEARCH":
                print "While looking around, you find a set of tracks leading from the edge of the moat. It looks like they have come from a sewer grate on the side of the castle, which has been busted open. You could fit inside, but it's quite a distance to jump, way more than most people can."
                print "What do you doest?"
            elif act.upper()=="JUMP TO HOLE" or act.upper()=="JUMP IN HOLE":
                print "You brace yourself, take a few steps back, and then take a running jump towards the grate!"
                if ply_sts.get("STRENGTH")<12:
                    print "Well damn young hero, I guess you shouldn't have skipped leg day so many times."
                    print "You leap forwards with all your strength, but unfortunately all your strength isn't enough strength."
                    print "You plummet into the water, and are eaten by horrendously large shark-bears."
                    return("Death")
                else:
                    print "Grass and mud tears up beneath your feet as you leap forwards with great power!"
                    print "You slam into the wall, and scrabbling for a handhold, you manage to grasp it, and climb in."
                    #enter dungeon
                    return ("Dungeon",ply_sts)
class Grand_Hall(Scene):

    def enter(self,ply_sts):
        pass

class Pantry(Scene):

    def enter(self,ply_sts):
        pass

class Armory(Scene):

    def enter(self,ply_sts):
        pass

class Dungeon(Scene):

    def enter(self,ply_sts):
        pass

class Throne_Room(Scene):

    def enter(self,ply_sts):
        pass

    def battle(self):
        pass

class fin(Scene):

    def enter(self,ply_sts):
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
            'fin':fin()
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
