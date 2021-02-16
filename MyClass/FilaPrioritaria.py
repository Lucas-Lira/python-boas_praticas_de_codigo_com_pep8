# Utilizando PEP-8
# =====================================================================

from typing import Dict, List, Union

from MyClass.fila_base import FilaBase

from MyClass.constantes import CODIGO_PRIORITARIO

class FilaPrioritaria(FilaBase):
    
    def gera_senha_atual(self)->None: # Indicando o retorno
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'
    
    def chama_cliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual {cliente_atual}, dirija-se ao caixa {caixa}'
    
    def estatistica(self, dia:str, agencia:int, retorna_estatistica):
        estatistica = retorna_estatistica(dia, agencia)
        return estatistica.executa(self.clientes_atendidos)