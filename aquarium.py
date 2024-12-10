import math
import random
def randomizer():
        return [random.randint(0, 9), random.randint(0, 9)]
    
class aquarium():
    def __init__(self, aquariumHeight, aquariumWidth):
        self.height = aquariumHeight
        self.width = aquariumWidth
        self.objList = []
        
class wobject():
    def __init__(self, x = 0, y = 0, appearance = 'abracadabra'):
        self.x = x
        self.y = y
        self.appearance = appearance
        
class memory():
    def __init__(self, vision, dx, dy, goodness = 0):
        self.vision = vision
        self.dx = dx
        self.dy = dy
        self.goodness = goodness

class fish():
    def __init__(self, hunger = 0, x=0, y=0, angle = 0, appearance = 'abracadabra'):
        self.hunger = hunger
        self.x = x
        self.y = y
        self.vision = []
        self.shortmemory = []
        self.longmemory = []
        self.radius = 1
        self.temporarystomach = []
        self.pain = 0
        self.appearance = appearance
        self.angle = angle
        
    def createMemory(self):
        xinit = self.x
        yinit = self.y
        visioninit = self.vision
        temporarystomach = []
        pain = 0
        newMemory = memory(visioninit, xinit, yinit)
        self.shortmemory.append(newMemory)
        
    def stopMemoryAndSave(self):
        xout = self.x
        yout = self.y
        visionout = self.vision
        if self.temporarystomach:
            self.shortmemory[len(self.shortmemory)-1].goodness += len(self.temporarystomach)
        if self.pain > 0:
            self.shortmemory[len(self.shortmemory)-1].goodness -= self.pain
        self.shortmemory[len(self.shortmemory)-1].dx = self.shortmemory[len(self.shortmemory)-1].dx - xout
        self.shortmemory[len(self.shortmemory)-1].dy = self.shortmemory[len(self.shortmemory)-1].dy - yout
        self.longmemory.append(self.shortmemory)
    
    def see(self, aquarius, distance= 2,  apperture = 2):
        x =self.x
        y =self.y
        self.vision = []
        vision= self.vision
        angle=self.angle
        for obj in aquarius.objList :
            #escrever o código para a visão de cone posteriormente
            if obj.x <= x + distance * math.cos(angle) and obj.x >= x*math.cos(angle) and obj.y <= y + apperture*math.sin(angle) and obj.y >= y+ y*math.sin(angle):
                vision.append(obj)  
    
    def remember(self, fog=2):
        situation = [self.x, self.y]
        longmemory = self.longmemory
        for moment in longmemory:
            if memory.x - fog < situation.x and memory.x + fog > situation.x and memory.y - fog < situation.y and memory.y + fog > situation.y:
                if memory.goodness > 0:
                    return [memory.x, memory.y]
                else:
                    if memory.goodness < 0:
                        return [-memory.x, -memory.y]
                    return randomizer()
            else:
                return randomizer()
        return randomizer()

    def move(self, act):
        self.x += act[0]
        self.y += act[1]
        
    def eat(self, aquarius, radius=2):
        x = self.x
        y =self.y
        for obj in aquarius.objList:    
            if obj.x - radius < x and obj.x + radius > x and obj.y - radius < y and obj.y + radius > y:
                self.temporarystomach.append(obj)

    def hurt(self):
        self.pain -= 1
        
aquario = aquarium(100, 100)
jeraldo = fish()
aquario.objList.append(jeraldo)
jeraldo.see(aquario)
jeraldo.createMemory()
act = jeraldo.remember()
print(act)
jeraldo.move(act)
#jeraldo.hurt()
jeraldo.eat(aquario)
jeraldo.stopMemoryAndSave()


mario = fish(1, jeraldo.x+1,jeraldo.y,90,'Andrade')
luigi = fish(1, jeraldo.x-1,jeraldo.y,0,'Mansion')
aquario.objList.append(mario)
aquario.objList.append(luigi)
