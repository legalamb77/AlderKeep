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
        boon = raw_input(">>").upper()
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
        current_scene=self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('fin')
        while current_scene!=last_scene:
            #current_scene.enter() needs to return (name of the next scene,stats)
            print stats
            print current_scene
            next_scene_name,new_stats=current_scene.enter(stats)
            stats=new_stats
            current_scene=self.scene_map.next_scene(next_scene_name)
        current_scene.enter(stats)

def drop(item,ply_sts):
    if item==1:
        ply_sts["SLOT_ONE"]=="NA"
        return ply_sts
    else:
        ply_sts["SLOT_TWO"]=="NA"
        return ply_sts

#Adds an item to the inventory, possibly calling drop to prompt player to drop an item
def take(item,ply_sts):
    if ply_sts.get("SLOT_ONE")=="NA":
        ply_sts["SLOT_ONE"]=item
        print "You pick up "+item
        return ply_sts
    elif ply_sts.get("SLOT_TWO")=="NA":
        ply_sts["SLOT_TWO"]=item
        print "You pick up "+item
        return ply_sts
    else:
        print "Your backpack is full! Which Slot would you like to drop from?"
        print "Slot one contains "+ply_sts.get("SLOT_ONE")
        print "Slot two contains "+ply_sts.get("SLOT_TWO")
        print "Enter 1, 2, or NA."
        act=raw_input(">>")
        if act==1:
            return drop(1,ply_sts)
        elif act==2:
            return drop(2,ply_sts)
        elif act.upper()==NA:
            print "Ah well, you leave "+item+" behind."
            return ply_sts
        else:
            print "WHAT ARE YOU SAYING. I CAN NOT UNDERSTAND YOU. PLEASE."
            return ply_sts


#Checks if a player has an item(for solving puzzles), returns True if they do, False otherwise
def check(item,ply_sts):
    if ply_sts.get("SLOT_ONE")==item:
        return True
    else:
        return False

class Death(Scene):

    def enter(self,ply_sts):
        print "You have died an ignoble death, the land shall be terrorized forevermore."
        exit(1)

class Drawbridge(Scene):

    def __init__(self):#, ply_sts):
        print "Enter Drawbridge."

    def enter(self,ply_sts):
        print "The rain batters down on your mother's armor(Unfortunately she left no sword) as you are confronted with the sprawling home of the LICH KING, known only as ALDER KEEP."
        print "The drawbridge is raised, and the moat churns with dark shapes in the water. Lurid light pours from several small windows about the walls of the keep. A small boat lies wrecked against the trees, tossed by some great power. It is completely destroyed, but a rope is strewn amongst it."
        print "The grass is slick with mud underfoot, and the road you came in on is but a dirt path. A number of trees line the edges of the moat."
        print "What dost thou do?"
        ropeTaken=False
        while True:
            act=raw_input(">>")
            if act.upper()=="LOOK" or act.upper()=="EXAMINE" or act.upper()=="SEARCH":
                print "While looking around, you find a set of tracks leading from the edge of the moat. It looks like they have come from a sewer grate on the side of the castle, which has been busted open. You could fit inside, but it's quite a distance to jump, way more than most people can."
                print "What do you doest?"
            elif act.upper()=="TAKE ROPE" and ropeTaken==False:
                print "You pick up the rope."
                ropeTaken==True
                if ply_sts.get("SLOT_ONE")=="NA":
                    ply_sts["SLOT_ONE"]="ROPE"
            elif act.upper()=="JUMP TO WINDOW" and (ply_sts.get("SLOT_ONE")=="ROPE" or ply_sts.get("SLOT_TWO")=="ROPE"):
                print "You take your rope and throw it to the window, using it to swing over easily and clamber up!"
                return ("Pantry",ply_sts)
            elif act.upper()=="JUMP TO WINDOW" and ply_sts.get("SLOT_ONE")!="ROPE" and ply_sts.get("SLOT_TWO")!="ROPE":
                print "The window is very far to jump to, unless you had something to bridge the gap, or if you're very strong."
                print "Do you want to try and jump?"
                act2=raw_input(">>")
                if act2.upper()=="YES" or act2.upper()=="Y":
                    if ply_sts.get("STRENGTH")<12 and ply_sts.get("SLOT_ONE")!="ROPE" and ply_sts.get("SLOT_TWO")!="ROPE":
                       print "You leap, and you fail. Sucks to be you, hero. The shark bears infesting the waters devour you."
                    else:
                        if (ply_sts.get("SLOT_ONE")=="ROPE" or ply_sts.get("SLOT_TWO")=="ROPE"):
                            print "You swing the rope up onto a branch, and use it to swing towards the window!"
                            if ply_sts.get("SLOT_ONE")=="ROPE":
                                ply_sts["SLOT_ONE"]="NA"
                            elif ply_sts.get("SLOT_TWO")=="ROPE":
                                pl_sts["SLOT_TWO"]="NA"
                        print "You fly like an eagle, and roll straight through the window!"
                        #enter pantry
                        return ("Pantry",ply_sts)
                elif act2.upper()=="NO" or act2.upper()=="N":
                    print "probably a smart choice."
                else:
                    print "Well, I'll take that as a no."
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
            else:
                print "Sorry, I don't understand."
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
        print "You stumble through the darkness, slipping on wet cobblestones strewn with brittle bones and moist fungus."
        print "Soon, you enter a pool of lurid light, cast by a single roughshod lantern hanging from a crude hook on the wall."
        print "There is a small table stained dark red with some substance, one you don't care to investigate."
        print "Three cells sit in a row along the north wall, two opened. One door sits to your east, made of wood and shut."
        print "The cells are labeled A, B, and C. The one labelled C is still closed."
        print "What do you do?"
        LanternTaken=False
        HookTaken=False
        while True:
            act=raw_input(">>").upper()
            if act=="TAKE LANTERN" or act=="GET LANTERN":
                print "You grab the lantern off the hook."
                if ply_sts.get("SLOT_ONE")=="NA" and ply_sts.get("SLOT_TWO")=="NA":
                    ply_sts["SLOT_ONE"]="LANTERN"
                    LanternTaken=True
                elif ply_sts.get("SLOT_ONE")!="NA" and ply_sts.get("SLOT_TWO")=="NA":
                    ply_sts["SLOT_TWO"]="LANTERN"
                    LanternTaken=True
                else:
                    print "Your hands are full, so you put it back."
            elif act=="TAKE HOOK" or act=="GET HOOK":
                if ply_sts.get("STRENGTH")>=18:
                    print "You rip that hook right outta the stone. You're strong as hell."
                    if ply_sts.get("SLOT_ONE")=="NA" and ply_sts.get("SLOT_TWO")=="NA":
                        ply_sts["SLOT_ONE"]="HOOK"
                        HookTaken=True
                    elif ply_sts.get("SLOT_ONE")!="NA" and ply_sts.get("SLOT_TWO")=="NA":
                        ply_sts["SLOT_TWO"]="HOOK"
                        HookTaken=True
                    else:
                        print "Your hands are full, do you want to drop something? If yes, tell me 1 or 2."
                        act2=raw_input(">>").upper()
                        if act2=="1":
                            print "Cool, you throw that thing away and take the new thing instead."
                            ply_sts["SLOT_ONE"]="HOOK"
                            HookTaken=True
                        elif act2=="2":
                            print "Cool, you throw that thing away and take the new thing instead."
                            ply_sts["SLOT_TWO"]="HOOK"
                            HookTaken=True
                        else:
                            print "You put it back though, your hands are full."
                else:
                    print "You tug on it, but it doesn't come out."
            else:
                print "Sorry, I don't understand."

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
            'Dungeon':Dungeon(),
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
