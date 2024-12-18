from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

# Create the Flask application
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST", "GET"])
def emotion_detection():
    if request.method == "POST":
        # Get the input JSON
        data = request.json
        if not data or "text" not in data:
            return jsonify({"error": "Invalid input. Please provide 'text' key in JSON."}), 400

        # Extract the text to analyze
        text_to_analyze = data["text"]
        result = emotion_detector(text_to_analyze)

        # Handle the case where the dominant emotion is None
        if result["dominant_emotion"] is None:
            return jsonify({"response": "Invalid text! Please try again!"})

        # Format the response
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"response": response_text})

    # Render the index.html template for GET requests
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)