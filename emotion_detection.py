
import requests  # Import the requests library for making HTTP requests

# API endpoint and headers provided by the task
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    
    # Prepare the input JSON as required by the API
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send a POST request to the Watson NLP API
        response = requests.post(URL, headers=HEADERS, json=input_json)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response and return the 'text' attribute
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return {"error": str(e)}

if __name__ == "__main__":
    # Example text to analyze
    test_text = "I am feeling so happy and joyful today!"
    result = emotion_detector(test_text)
    print(result)



