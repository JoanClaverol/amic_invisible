from random import choice, shuffle

class generador_amic_invisible(): 

    def __init__(self, amics: list): 
        self.amics = amics

    def genera_flat_amics(self):
        self.flat_amics = []
        self.parelles = []
        self.solters = []
        for amic in self.amics: 
            if type(amic) is list: 
                parella_seleccionada = []
                for parella in amic: 
                    self.flat_amics.append(parella.lower())
                    parella_seleccionada.append(parella.lower())
                self.parelles.append(parella_seleccionada)
            else: 
                self.flat_amics.append(amic.lower())
                self.solters.append(amic.lower())
        shuffle(self.flat_amics)

    def trobar_parella(self, persona):
        persona = persona.lower() 
        for parella in self.parelles: 
            if persona in parella: 
                self.parella = [nom for nom in parella if nom != persona][0]
                break
            else: 
                self.parella = None

    def genera_amics_invisibles(self): 
        
        self.genera_flat_amics()
        self.amics_invisibles = []
        resta_amic_inv = self.flat_amics.copy()
        for amic in self.flat_amics: 
            print(amic)
            amic_seleccionat = amic
            self.trobar_parella(amic)
            # try: 
            counter = 0
            while amic_seleccionat == amic or amic_seleccionat == self.parella:
                counter += 1
                amic_seleccionat = choice(resta_amic_inv)
                print(f'{amic} {self.parella} {amic_seleccionat}')
                if counter > len(self.flat_amics) * 5: 
                    self.genera_amics_invisibles()
                    break
            self.amics_invisibles.append([amic, amic_seleccionat])
            resta_amic_inv.remove(amic_seleccionat)
            print(resta_amic_inv)
            # except: 
            #     self.genera_amics_invisibles()

amics = [
    ['Jordi', 'MCarmen'],
    'Yayo', 
    'Cristina',
    'Alex',
    'Joel',
    ['Alberto','Pili'],
    ['Roger','Txell'],
    ['Joan','Nuria']
]

c = generador_amic_invisible(amics)
c.genera_amics_invisibles()
print(c.amics_invisibles)
