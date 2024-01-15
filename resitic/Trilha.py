from dataclasses import dataclass
from resitic import Residente
import pandas as pd

@dataclass
class Trilha():
    __residentes: pd.DataFrame
    __nome: str
    
    def __init__(self, nome: str = None):
        self.__residentes = pd.DataFrame(columns=['identificador', 'idade', 'formacao', 'formacaoGeral', 'formacaoEspecifica', 'andamentoGraduacao', 'tempoFormacao', 'experienciaPrevia'])
        self.__nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def residentes(self) -> list[Residente]:
        return self.__residentes
    
    def addResidente(self, residente: Residente) -> None:
        if not isinstance(residente, Residente):
            raise TypeError("Residente não é do tipo Residente")
        
        if residente.identificador in self.residentes['identificador']:
            raise ValueError("Residente já cadastrado")
        
        residente_dict = {
            'identificador': residente.identificador,
            'idade': residente.idade,
            'formacao': residente.formacao,
            'formacaoGeral': residente.formacaoGeral,
            'formacaoEspecifica': residente.formacaoEspecifica,
            'andamentoGraduacao': residente.andamentoGraduacao,
            'tempoFormacao': residente.tempoFormacao,
            'experienciaPrevia': residente.experienciaPrevia
        }
        
        residente_df = pd.DataFrame(residente_dict)
        
        self.residentes = pd.concat([self.residentes, residente_df])