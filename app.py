from flask import Flask, render_template, request
from flowIA import langflow_call

app = Flask(__name__)
@app.route('/')
def dashboard():
    # Dados simulados para exibição
    campaigns = [
        {'name': 'Campanha de Verão', 'status': 'Ativa'},
        {'name': 'Promoção de Inverno', 'status': 'Pausada'},
        {'name': 'Lançamento de Produto', 'status': 'Concluída'},
    ]
    return render_template('dashboard.html', campaigns=campaigns)
@app.route('/newsletter', methods=['GET', 'POST'])
def newsletter():
    generated_newsletter = None
    if request.method == 'POST':
        theme = request.form['theme']
        link = request.form['link']
        generated_newsletter = langflow_call(theme, link)
        
    return render_template('newsletter.html', generated_newsletter=generated_newsletter)
if __name__ == '__main__':
    app.run(debug=True)

