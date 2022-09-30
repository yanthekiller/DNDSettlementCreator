import random

class NameGenerate:
    alphabet=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    alphabet_soglas=['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ъ','ь']
    alphabet_glas=['а','е','ё','и','о','у','ы','э','ю','я']
    result=''
    finaleResult=[]
    def generate(self, amount):
        for iter in range(amount):
            length=random.randint(3,9)
            for i in range(length):
                self.result+=self.alphabet[random.randint(0,len(self.alphabet)-1)]
                pass
            self.checkErrors()
            #print(self.result)
            self.finaleResult.append(self.result)
            self.result=''
        print(self.finaleResult)
        return self.finaleResult

    def checkErrors(self):
        if self.result[0]=='ъ' or self.result[0]=='ь' or self.result[0]=='ы':
            self.result=self.alphabet_soglas[random.randint(0,len(self.alphabet_soglas)-1)]+self.result[1:]
        if self.result[1]=='ъ' or self.result[1]=='ь':
            if self.glassoglas(self.result[0])==False:
                result=self.alphabet_soglas[random.randint(0,len(self.alphabet_soglas)-1)]+self.result[1:]
        isChanged=True
        while isChanged==True:
            try:
                isChanged=False
                for item in range(len(self.result)):
                    if self.glassoglas(self.result[item])==True:
                        if self.glassoglas(self.result[item+1])==True:
                            if self.glassoglas(self.result[item+2])==True:
                                self.result=self.result[:item+1]+self.alphabet_glas[random.randint(0,len(self.alphabet_glas)-1)]+self.result[item+2:]
                                isChanged=True
                    else:
                        if self.glassoglas(self.result[item+1])==False:
                            if self.glassoglas(self.result[item+2])==False:
                                self.result=self.result[:item+1]+self.alphabet_soglas[random.randint(0,len(self.alphabet_soglas)-1)]+self.result[item+2:]
                                isChanged=True
                    if self.result[item]=='ь' or self.result[item]=='ъ':
                        if glassoglas(self.result[item-1])==False:
                            self.result=self.result[:item-2]+self.alphabet_glas[random.randint(0,len(self.alphabet_soglas)-1)]+self.result[item:]
                            isChanged=True
            except Exception as e:
                #print(e.__str__())
                #isChanged=True
                pass
                    
    def glassoglas(self, letterToCheck):
        for i in self.alphabet_soglas:
            if i==letterToCheck:
                return True
        return False

    pass

gen=NameGenerate()
#gen.generate(100)

