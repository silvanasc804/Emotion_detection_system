
from flask import Flask, render_template, request, redirect, url_for
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.sentiment_analysis import sentiment_analyzer

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis and emotion detection over it using emotion_detector()
        function. The output returned shows the information for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    s_response = sentiment_analyzer(text_to_analyze)
    label = s_response['label']
    score = s_response['score']
    
    e_response= emotion_detector(text_to_analyze)
    anger = e_response['anger']
    disgust = e_response['disgust']
    fear = e_response['fear']
    joy = e_response['joy']
    sadness = e_response['sadness']
    dominant_emotion =  e_response['dominant_emotion']
    
    if label is None:
        return "Invalid input ! Try again."
    elif dominant_emotion is None:
        return "Invalid text! Please try again!."
    else:
        return f"The given text has been identified as {label.split('_')[1]} with a score of {score}.\nAnd the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."
    
  

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="localhost", port=5000)