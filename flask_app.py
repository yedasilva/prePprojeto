import banco
import carrinho_html
import produtos_html
from flask import Flask

app = Flask(__name__)


@app.route('/')
def principal():
    produtos = banco.consulta_produtos()
    pag = produtos_html.gerar_html_produtos(produtos)
    return pag

@app.route('/carrinho')
def comprar():
   carrinho = banco.consulta_produtos()
   comp = carrinho_html.gerar_html_carrinho(carrinho)
   return comp


#############################################
#
# ao copiar seu codigo para o pythonanywhere, remover as linhas abaixo!
#
#############################################


if __name__ == '__main__':
  app.run(debug=True, use_debugger=False, use_reloader=False)