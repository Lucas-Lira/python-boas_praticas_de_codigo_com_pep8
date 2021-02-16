import abc
from typing import List

from MyClass.constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO

class FilaBase:

    codigo: int = 0
    fila: List[str] = [] 
    clientes_atendidos: List[str] = []
    senha_atual: str = ''
        
    def insere_cliente(self):
        self.fila.append(self.senha_atual)
          
    def reseta_fila(self)->None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1
            
    def atualiza_fila(self)->None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()
            
    @abc.abstractmethod
    def gera_senha_atual(self)->None:
        ...
        
    @abc.abstractmethod
    def chama_cliente(self, caixa:int)->str:
        ...