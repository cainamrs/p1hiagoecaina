from flask import Flask, render_template, request


# Cria a aplicação Flask
app = Flask(__name__)


# Rota principal.
# Aceita tanto GET quanto POST.
@app.route("/", methods=["GET", "POST"])
def index():

# Variáveis que serão usadas para mostrar o resultado
nome = ""
imc = None
faixa = ""
cor_alerta = ""

# Lista onde vamos guardar TODOS os erros encontrados
erros = []

# Só entra aqui quando o formulário for enviado
if request.method == "POST":

# Pega os dados enviados pelo formulário
nome = request.form.get("nome", "").strip()
peso_texto = request.form.get("peso", "").strip()
altura_texto = request.form.get("altura", "").strip()

# Validação do nome
if not nome:
erros.append("Informe o nome.")

# Validação do peso
peso = None

if not peso_texto:
erros.append("Informe o peso.")
else:
try:
peso = float(peso_texto)

if peso <= 0:
erros.append("O peso deve ser maior que 0.")

elif peso > 300:
erros.append("O peso deve ser de até 300 kg.")

except ValueError:
erros.append("O peso deve ser um número válido.")

# Validação da altura
altura = None

if not altura_texto:
erros.append("Informe a altura.")
else:
try:
altura = float(altura_texto)

if altura < 0.5 or altura > 2.5:
erros.append(
"A altura deve estar entre 0,5 e 2,5 metros."
)

except ValueError:
erros.append("A altura deve ser um número válido.")

# Só calcula se não existir nenhum erro
if not erros:

# Fórmula do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
faixa = "Abaixo do peso"
cor_alerta = "info"

elif imc < 25:
faixa = "Peso normal"
cor_alerta = "success"

elif imc < 30:
faixa = "Sobrepeso"
cor_alerta = "warning"

else:
faixa = "Obesidade"
cor_alerta = "danger"

# Envia os dados para o HTML
return render_template(
"index.html",
nome=nome,
imc=imc,
faixa=faixa,
cor_alerta=cor_alerta,
erros=erros
)


# Rota da página da equipe
@app.route("/equipe")
def equipe():

return render_template(
"equipe.html",
nome1="SEU NOME",
ra1="SEU RA",
nome2="NOME DO COLEGA",
ra2="RA DO COLEGA",
repositorio="https://github.com/SEU-USUARIO/avaliacao-imc"
)


# Inicia o servidor
if __name__ == "__main__":
app.run(debug=True)
