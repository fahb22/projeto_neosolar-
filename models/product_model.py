# models/product_model.py
import pandas as pd

class ProductModel:
    def __init__(self):
        self.produtos = [
            {"Categoria": "Painel Solar", "Id": 1001, "Potencia em W": 500, "Produto": "Painel Solar 500 W Marca A"},
            {"Categoria": "Painel Solar", "Id": 1002, "Potencia em W": 500, "Produto": "Painel Solar 500 W Marca B"},
            {"Categoria": "Painel Solar", "Id": 1003, "Potencia em W": 500, "Produto": "Painel Solar 500 W Marca C"},
            {"Categoria": "Controlador de carga", "Id": 2001, "Potencia em W": 500, "Produto": "Controlador de Carga 30A Marca E"},
            {"Categoria": "Controlador de carga", "Id": 2002, "Potencia em W": 750, "Produto": "Controlador de Carga 50A Marca E"},
            {"Categoria": "Controlador de carga", "Id": 2003, "Potencia em W": 1000, "Produto": "Controlador de Carga 40A Marca D"},
            {"Categoria": "Inversor", "Id": 3001, "Potencia em W": 500, "Produto": "Inversor 500W Marca D"},
            {"Categoria": "Inversor", "Id": 3002, "Potencia em W": 1000, "Produto": "Inversor 1000W Marca D"}
        ]
        self.df_produtos = pd.DataFrame(self.produtos)
        self.geradores = []

    def criar_geradores(self):
        id_gerador = 11111
        paineis = self.df_produtos[self.df_produtos['Categoria'] == 'Painel Solar']
        inversores = self.df_produtos[self.df_produtos['Categoria'] == 'Inversor']
        controladores = self.df_produtos[self.df_produtos['Categoria'] == 'Controlador de carga']

        for _, painel in paineis.iterrows():
            for _, inversor in inversores.iterrows():
                for _, controlador in controladores.iterrows():
                    if painel['Potencia em W'] == inversor['Potencia em W'] == controlador['Potencia em W']:
                        gerador = {
                            'ID Gerador': id_gerador,
                            'Potência do Gerador (em W)': painel['Potencia em W'],
                            'ID Produto': [painel['Id'], inversor['Id'], controlador['Id']],
                            'Nome do Produto': [painel['Produto'], inversor['Produto'], controlador['Produto']],
                            'Quantidade Item': [1, 1, 1]
                        }
                        self.geradores.append(gerador)
                        id_gerador += 1
        return self.geradores
