from flask import Flask, request, render_template_string

app = Flask(__name__)

def somar(a: float, b: float) -> float:
    return a + b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Simples</title>
    <style>
        body { font-family: sans-serif; margin: 40px; }
        input, select, button { padding: 8px; margin: 5px; }
    </style>
</head>
<body>
    <h2>App de Teste da Esteira</h2>
    <form method="POST" action="/">
        <input type="number" name="a" step="any" required placeholder="Número A">
        <select name="operacao">
            <option value="somar">+</option>
            <option value="dividir">/</option>
        </select>
        <input type="number" name="b" step="any" required placeholder="Número B">
        <button type="submit">Calcular</button>
    </form>
    
    {% if resultado is not none %}
        <h3 style="color: green;">Resultado: {{ resultado }}</h3>
    {% endif %}
    
    {% if erro %}
        <h3 style="color: red;">Erro: {{ erro }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            op = request.form.get("operacao")
            
            if op == "somar":
                resultado = somar(a, b)
            elif op == "dividir":
                resultado = dividir(a, b)
        except ValueError as e:
            erro = str(e) if "Divisão" in str(e) else "Entrada inválida. Digite apenas números."
            
    return render_template_string(html_template, resultado=resultado, erro=erro)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)