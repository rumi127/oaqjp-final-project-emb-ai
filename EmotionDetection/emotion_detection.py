import requests
import json

# Watson NLP API details
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    Detect emotions in text and format the output with the dominant emotion.
    Args:
        text_to_analyze (str): Text to analyze for emotions.
    Returns:
        dict: Emotions with scores and the dominant emotion.
    """
    if not text_to_analyze.strip():
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send a POST request to Watson NLP API
        response = requests.post(URL, headers=HEADERS, json=input_json)
        if response.status_code == 400:
            return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
        }

        # Convert response to a Python dictionary
        response_data = response.json()


        # Extract emotion scores
        emotion_predictions = response_data.get("emotionPredictions", [])
        if emotion_predictions:
            raw_emotions = emotion_predictions[0].get("emotion", {})

            # Find the dominant emotion
            dominant_emotion = max(raw_emotions, key=raw_emotions.get)

            # Format the output
            formatted_output = {
                "anger": raw_emotions.get("anger", 0),
                "disgust": raw_emotions.get("disgust", 0),
                "fear": raw_emotions.get("fear", 0),
                "joy": raw_emotions.get("joy", 0),
                "sadness": raw_emotions.get("sadness", 0),
                "dominant_emotion": dominant_emotion,
            }
            return formatted_output
        return {"error": "No emotion predictions found"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    text = "I am so happy and excited!"
    result = emotion_detector(text)
    print(result)

