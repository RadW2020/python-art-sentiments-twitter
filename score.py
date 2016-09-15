# coding: utf-8
import tweepy
import json
from tweepy import OAuthHandler
from watson_developer_cloud import ToneAnalyzerV3

#Constantes para facilitar el acceso al JSON que retonrna el Tone Analyzer
EMOTION_TONE = 0
LANGUAGE_TONE = 1
SOCIAL_TONE = 2

ANGER = 0
DISGUST = 1
FEAR= 2
JOY = 3
SADNESS = 4

class ScoreTweets:

    def __init__(self):
        #claves de autenticacion API TWITTER
        self.consumer_key = ''
        self.consumer_secret = ''
        self.access_token = ''
        self.access_secret = ''

        #claves de autenticacion de Tone Analyzer
        self.tone_analyzer = ToneAnalyzerV3(username='',
        password='',
        version='2016-05-19')

    def start(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth)

    #Mostramos el ampo TEXT del tweet, eliminando la informacion irrelevante para este ejemplo
    def _process_or_store(self, tweet):
        #print(json.dumps(tweet['text']).encode('utf8'))
        textTweet = json.dumps(tweet['text']).encode('utf8')
        print("Text: " + textTweet)
        #print(tone_analyzer.tone(textTweet)["document_tone"]["tone_categories"][EMOTION_TONE]["tones"][0]["score"])
        arraySentimientos = []
        for i in range(0,5):
            scoreEmotion = self.tone_analyzer.tone(textTweet)["document_tone"]["tone_categories"][EMOTION_TONE]["tones"][i]["score"]
            arraySentimientos.append(scoreEmotion)
        return arraySentimientos

    def getValues(self, username):
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=username).items():
            arrayValues = []
            arrayValues = self._process_or_store(tweet._json)
            return arrayValues
