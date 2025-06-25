import os
from google.cloud import dialogflow_v2 as dialogflow

#path to downloaded JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Dell/coding/Benchmark/healthcare_bot/demoagent-wgo9-38b8fd98fea6.json"


project_id = 'demoagent-wgo9'  

def create_custom_intent(display_name, training_phrases_parts, message_text):
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"

    training_phrases = []
    for phrase in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
        training_phrases.append(dialogflow.Intent.TrainingPhrase(parts=[part]))
    
    text = dialogflow.Intent.Message.Text(text=[message_text])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = client.create_intent(request={'parent': parent, 'intent': intent})
    print(f"✅ Created intent: {display_name}")

# Example usage:
create_custom_intent('Location - Vague', ["I want nearby service", "any clinic near me"], "Could you please specify your preferred location?")
