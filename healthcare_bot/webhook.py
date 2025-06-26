# webhook.py

from flask import Flask, request, jsonify
from db_logger import log_conversation
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print("✅ Webhook triggered")
    print("👉 Incoming request:", req)
    
    # 🔍 Extract user message and intent
    user_message = req['queryResult']['queryText']
    bot_response = req['queryResult']['fulfillmentText']
    intent_name = req['queryResult']['intent']['displayName']
    session_id = req['session'].split('/')[-1]

    # ✅ Log to MySQL
    log_conversation(session_id, user_message, bot_response, intent_name)

    return jsonify({'fulfillmentText': bot_response})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

