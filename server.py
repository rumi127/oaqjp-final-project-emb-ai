from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

# Instantiate the Flask app
app = Flask(__name__)

# Define the route for the EmotionDetector API
@app.route("/emotionDetector", methods=["POST", "GET"])
def emotion_detection():
    if request.method == "POST":
        # Extract the text from the POST request
        data = request.json
        if not data or "text" not in data:
            return jsonify({"error": "Invalid input. Please provide 'text' key in JSON."}), 400

        text_to_analyze = data["text"]

        # Get the emotion detection result
        result = emotion_detector(text_to_analyze)

        # Format the response
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"response": response_text})

    return render_template("index.html")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
