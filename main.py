from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configurar API Key de OpenAI
openai.api_key = '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'

# Lista para almacenar conversaciones
conversations = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global conversations
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST' and request.form['question']:
        # Obtener la pregunta del usuario
        question = 'Yo: ' + request.form['question']

        # Generar respuesta con OpenAI API
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.5,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        # Almacenar la pregunta y respuesta en la lista de conversaciones
        answer = 'AI: ' + response.choices[0].text.strip()
        conversations.append(question)
        conversations.append(answer)

        # Renderizar plantilla HTML con la conversación actualizada
        return render_template('index.html', chat=conversations)
    elif request.method == 'POST' and request.form['new_conversation'] == 'true':
        # Borrar la lista de conversaciones
        conversations = []

        # Renderizar plantilla HTML con la conversación vacía
        return render_template('index.html', chat=conversations)
    else:
        # Si el usuario no envía una pregunta, renderizar la plantilla HTML sin cambios
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)