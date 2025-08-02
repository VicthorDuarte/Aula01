#framework moderno e rapido para construção de API RESTFUL com python.
'''
i. Pydantic - validação via tipagem
ii.Starlette - servidor assincrono de alto desempenho
iii.OpenAI - geração automática de documentação
'''
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, Body, Path, Query
app = FastAPI(title='Calculadora',
              dscription = 'Calculadora criada com swagger em fast api',
              version='1.0.0',
              servers= [{'url':'http://127.0.0.1:8000'},{'url':'http://127.0.0.1:8001'}],
              swagger_ui_oauth2_redirect_url = "/Swagger/oauth2-redirect",
              docs_url='/Swagger',
              openapi_url='/FastApi_aula.json',
              )

@app.get('/')
def home():
    return{'mensagem':'Bem vindo ao FastAPI'}

class Item(BaseModel):
     nome: str = Field(..., title ='Nome do item', example= 'Creme')
     preco: float = Field(...,gt=0, example = '1,2,3,5')
     descricao: Optional[str] = Field (None, title = 'Descrição', example='descrição(ex): Creme de barbar bozano 250ml.')
     em_estoque: bool= Field(..., title='Verdadeiro ou falso', description= '''True = Disponibilidade no estoque
     \nFalse = Não disponivel no estoque''')

@app.post('/itens/',response_model=Item, summary='Criar novo item')
async def criar_item(item:Item = Body(...,example={
    "nome": 'Mouse',
    "preco": 20,
    "descricao:":"Mouse bom",
    "em_estoque": True
})):
    '''
    Cria um novo item no banco de dados ficticio.
    '''
    return item
    
@app.get('/itens/{item_id}', response_model = Item, summary = 'Buscar item por ID')
async def ler_item(
    item_id: int = Path(..., title = 'ID do item' , gt=0),
    detalhes: Optional[bool] = Query(False, description = 'Mostrar detalhes')
):
    '''
    Retorna um item do banco de dados ficticio usando o 'item_id'.
    
    -**item_id**: ID do item (Inteiro positivo)
    -**detalhes**: se True, mostra descrição do estoque
    '''
    return{
        "nome": 'Teclado',
        "preco": 20,
        "descricao:":"Teclado mecanico",
        "em_estoque": False
        }

@app.get('/soma')
def somar(a:int, b:int):
    return{'resultado': f'Resultado da soma foi: {a+b}'}

