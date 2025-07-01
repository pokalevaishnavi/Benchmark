# webhook.py

from flask import Flask, request, jsonify
from db_logger import log_conversation
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '✅ HealthcareBot Webhook is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print("✅ Webhook triggered")
    print("👉 Incoming request:", req)
    
    # 🔍 Extract user message and intent
    user_message = req['queryResult']['queryText']
    bot_response = req['queryResult'].get('fulfillmentText', '')
    intent_name = req['queryResult']['intent']['displayName']
    session_id = req['session'].split('/')[-1]

    # ✅ Log to MySQL
    log_conversation(session_id, user_message, bot_response, intent_name)
    
    if intent_name == "Default Welcome Intent":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Hi there! Welcome to our Healthcare Bot. How can I assist you today?"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "View Services" },
                        { "text": "Help" },
                        { "text": "Exit" }
                    ]}
                ]]}}
            ]
        })
    elif intent_name == "Select Service":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Please select a service:"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "Massage" },
                        { "text": "Spa Service" },
                        { "text": "Physiotherapy" },
                        { "text": "Doctor Consultation" }
                    ]}
                ]]}}
            ]
        })

    elif intent_name == "Select Location":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Select a preferred location:"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "Pune" },
                        { "text": "Mumbai" },
                        { "text": "Ratnagiri" },
                        { "text": "Kolhapur" }
                    ]}
                ]]}}
            ]
        })
        
    elif intent_name == "Confirm Location":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Select a preferred day:"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "Monday" },
                        { "text": "Tuesday" },
                        { "text": "Wednesday" },
                        { "text": "Thursday" }
                    ]}
                ]]}}
            ]
        })

    elif intent_name == "Select Date":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Choose a date for your appointment:"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "30 minutes" },
                        { "text": "45 minutes" },
                        { "text": "1 hour" },
                        { "text": "2 hour" }
                    ]}
                ]]}}
            ]
        })
        
    elif intent_name == "Book Slot by Duration":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Choose a preferred time slot:"] }},
                { "payload": { "richContent": [[
                    { "type": "chips", "options": [
                        { "text": "10:00 AM" },
                        { "text": "11:30 AM" },
                        { "text": "3:00 PM" },
                        { "text": "4:30 PM" }
                    ]}
                ]]}}
            ]
        })
        
    elif intent_name == "Confirm Booking":
        return jsonify({
            "fulfillmentMessages": [
                { "text": { "text": ["Your session has been booked!"] }},
               
            ]
        })


    return jsonify({'fulfillmentText': bot_response})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

