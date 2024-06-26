import pandas as pd
import plotly.express as px

dados = pd.read_csv('marketing_investimento.csv')

print(dados)

aderencia_investimento = px.histogram(dados, x='aderencia_investimento', text_auto=True)
aderencia_investimento.show()

estado_civil = px.histogram(dados, x='estado_civil', text_auto=True, color='aderencia_investimento', barmode='group')
estado_civil.show()

escolaridade = px.histogram(dados, x='escolaridade', text_auto=True, color='aderencia_investimento', barmode='group')
escolaridade.show()

inadimplencia = px.histogram(dados, x='inadimplencia', text_auto=True, color='aderencia_investimento', barmode='group')
inadimplencia.show()
