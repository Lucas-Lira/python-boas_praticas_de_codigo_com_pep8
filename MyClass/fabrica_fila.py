from typing import Union

from MyClass.fila_normal import FilaNormal
from MyClass.FilaPrioritaria import FilaPrioritaria
from MyClass.constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

class FabricaFila:
    
    @staticmethod
    def pega_fila(tipo_fila:str) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')