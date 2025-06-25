import os
from google.cloud import dialogflow_v2 as dialogflow

#path to downloaded JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"

project_id = 'demoagent-wgo9'  

def update_intent(intent_display_name, training_phrases_parts, message_text):
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"


    # List all intents to find the intent ID
    intents = client.list_intents(request={"parent": parent})
    
    for intent in intents:
        if intent.display_name == intent_display_name:
            # Update training phrases
            training_phrases = []
            for phrase in training_phrases_parts:
                part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
                training_phrases.append(dialogflow.Intent.TrainingPhrase(parts=[part]))
            
            # Update response message
            text = dialogflow.Intent.Message.Text(text=[message_text])
            message = dialogflow.Intent.Message(text=text)
            
            # Update intent fields
            intent.training_phrases = training_phrases
            intent.messages = [message]
            
            response = client.update_intent(request={'intent': intent, 'language_code': 'en'})
            print(f"✅ Updated intent: {intent_display_name}")
            return

    print(f"❌ Intent '{intent_display_name}' not found!")

# Example usage:
update_intent('Default Welcome Intent', ["Hello", "Hi there"], "Welcome to HealthBot!")
update_intent('Default Fallback Intent', ["random gibberish"], "Sorry, I didn't understand that.")
