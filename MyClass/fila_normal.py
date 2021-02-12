# Utilizando TypeHints
# =====================================================================
class fila_normal:
    codigo:int = 0 # Indicando o tipo do dado
    fila = []
    clientesatendidos = []
    senhaatual:str = ""
        
    def gerasenhaatual(self)->None: # Indicando o retorno
        self.senhaatual = f'NM{self.codigo}'
        
    def resetafila(self)->None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
            
    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)
        
    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return f'Cliente atual {cliente_atual}, dirija-se ao caixa {caixa}'
    
    def teste(self):
        print('Teste concluído!')