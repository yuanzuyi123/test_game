from python_practice.jinx import jinx1
from python_practice.ez import EZ
from python_practice.police import Police
from python_practice.timo import timo

class Hero_Factory:

    def create_hero(self,name):

        if name =='jinx':

            return jinx1()
        elif name =='EZ':

            return  EZ()
        elif name=='police':
            return  Police()
        elif name == 'timo':
            return  timo()
        else:
            raise Exception("此英雄不在英雄工厂里面")

    def  speak_lines(self,name):
        if  name =='police':
            print ("见识一下法律的子弹")

        elif name =='timo':
            print ("提莫队长正在待命")
        pass
hero = Hero_Factory()
# jinx=hero.create_hero("jinx")
# EZ=hero.create_hero("EZ")
timo = hero.create_hero("timo")
print (hero.speak_lines("timo"))
polic = hero.create_hero("police")
print (hero.speak_lines("police"))
#jinx.fight(EZ.hp,EZ.power)