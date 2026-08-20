from flask import Flask, render_template, request, jsonify

from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

@app.route('/subjects', methods=['GET'])
def get_subjects():
    """Get list of available subjects"""
    subjects = ['physics', 'chemistry', 'biology', 'government']
    return jsonify({'subjects': subjects})

if __name__ == '__main__':
    # Run on localhost at port 8000
    app.run(debug=True, host='127.0.0.1', port=8000)
