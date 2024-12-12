import math
import random
import pickle 

pi = math.pi
def load_aquario(aquarioname = 'aguario'):
     with open('aquario/'+aquarioname+".pkl", 'rb') as m:
        aquario = pickle.load(m)
        return aquario

def save_aquario(aquarior, name="aguario"):
    with open("aquario/"+name+'.pkl', 'wb') as outp:
        pickle.dump(aquarior, outp, pickle.HIGHEST_PROTOCOL)
    
def randomizer():
        return [random.randint(0, 9), random.randint(0, 9), random.uniform(0, 2*pi)]
    
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
    def __init__(self, vision, dx, dy, rotation, goodness = 0):
        self.vision = vision
        self.dx = dx
        self.dy = dy
        self.rotation = rotation
        self.goodness = goodness

class fish():
    def __init__(self, energy = 10, x=0, y=0, angle = 0, appearance = 'abracadabra'):
        self.energy = energy
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
        rotation = self.angle
        temporarystomach = []
        pain = 0
        newMemory = memory(visioninit, xinit, yinit, rotation)
        self.shortmemory.append(newMemory)
        
    def stopMemoryAndSave(self):
        xout = self.x
        yout = self.y
        visionout = self.vision
        rotationout = self.angle
        if self.temporarystomach:
            self.shortmemory[len(self.shortmemory)-1].goodness += len(self.temporarystomach)
        if self.pain > 0:
            self.shortmemory[len(self.shortmemory)-1].goodness -= self.pain
        self.shortmemory[len(self.shortmemory)-1].dx = self.shortmemory[len(self.shortmemory)-1].dx - xout
        self.shortmemory[len(self.shortmemory)-1].dy = self.shortmemory[len(self.shortmemory)-1].dy - yout
        self.shortmemory[len(self.shortmemory)-1].rotation = self.shortmemory[len(self.shortmemory)-1].rotation - rotationout
        self.longmemory.append(self.shortmemory)
    
    def see(self, aquarius, distance= 2,  apperture = 2):
        x =self.x
        y =self.y
        self.vision = []
        vision= self.vision
        angle=self.angle
        direita = (math.cos(angle) >= 0)
        esquerda = not direita
        cima = math.sin(angle) >= 0
        baixo = not cima
        for obj in aquarius.objList :
            dentro = True
            if direita:
                    if not ( obj.x <= x + distance * math.cos(angle) and obj.x >= x):
                        dentro = False
            else:        
                    if not (obj.x >= x + distance * math.cos(angle) and obj.x <= x):
                        dentro = False
            if cima:
                    if not (obj.y <= y + apperture*math.sin(angle) and obj.y >= y):
                        dentro = False
            else:
                    if not ( obj.y >= y + apperture*math.sin(angle) and obj.y <= y): 
                        dentro = False
            #escrever o código para a visão de cone posteriormente
            if dentro:
                vision.append(obj)  
    
    def remember(self, fog=2):
        situation = [self.x, self.y, self.angle]
        longmemory = self.longmemory
        for memory in longmemory:
            if not memory[0].vision:
                if memory[0].dx - fog < situation[0] and memory[0].dx + fog > situation[0] and memory[0].dy - fog < situation[1] and memory[0].dy + fog > situation[1]:
                    if memory[0].goodness > 0:
                        return [memory[0].dx, memory[0].dy, memory[0].rotation]
                    else:
                        if memory.goodness < 0:
                            return [-memory[0].dx, -memory[0].dy, memory[0].rotation]
                        return randomizer()
                else:
                    return randomizer()
            else:
                return randomizer()
        return randomizer()

    def move(self, act, aquario):
        self.energy -= 1
        if self.energy < 0:
                print("O peixe "+ self.appearance + " morreu")
                aquario.objList.remove(self)
                return
        self.x += act[0]
        self.y += act[1]
        self.angle += act[2]
        print("o peixe "+ self.appearance+" se moveu para "+ str([self.x, self.y]))
        
    def eat(self, aquarius, radius=2):
        x = self.x
        y =self.y
        for obj in aquarius.objList:    
            if obj.x - radius < x and obj.x + radius > x and obj.y - radius < y and obj.y + radius > y and obj !=self:
                self.temporarystomach.append(obj)
                aquarius.objList.remove(obj)
                self.energy +=1
                print(self.appearance + " comeu o "+obj.appearance)
                

    def hurt(self):
        self.pain -= 1

#é necessário salvar a situação do aquário em um arquivo
#fazer um programa que atualiza o aquário a cada n segundos
#e deixar ele rodando, (como fazer um código python ser executado de vez em quando? Posso fazer uso do servidor)
#e recarregar este aquário quando uma chamada é feita.
#enviando os dados para o navegador

def tick():
  aquario = load_aquario()
  for peixe in [peixe for peixe in aquario.objList if isinstance(peixe, fish)]:
        aquario = load_aquario()
        peixe.see(aquario)
        peixe.createMemory()
        act = peixe.remember()
        print("o peixe "+peixe.appearance+" se lembrou de quando fez..."+str(act))
        if peixe.energy < 5:
            peixe.eat(aquario)
        peixe.move(act, aquario)
        #peixe.hurt()
        peixe.stopMemoryAndSave()
        save_aquario(aquario)
        return get_aquarium()

def jogar_racao(x = None, y = None):
    aquario = load_aquario()
    for peixe in aquario.objList:
        if x == None:
            x = peixe.x+1
        if y == None:
            y = peixe.y+1
            racao = wobject(x, y, 'ração')
            aquario.objList.append(racao)
    save_aquario(aquario)

def create_fish(appearance, energy = 10, x = 0, y = 0):
    aquario = load_aquario()
    newFish = fish(energy, x, y, 0, appearance)
    aquario.objList.append(newFish)
    save_aquario(aquario)

def get_aquarium():
    aquario = load_aquario()
    generalAquarium = []
    for thing in aquario.objList:
         thingArray = []
         thingArray.append(thing.x)
         thingArray.append(thing.y)
         thingArray.append(thing.appearance)
         if type(thing) == fish:
              thingArray.append(thing.angle)
              thingArray.append(thing.energy)
              thingArray.append(thing.radius)

         generalAquarium.append(thingArray)
    return generalAquarium
