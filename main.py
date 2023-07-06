#import the packages
from newspaper import Article
import random
import string
import numpy as np
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')  #ignore the warnings

#download package from nltk
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)

#get artical url
article= Article('https://en.wikipedia.org/wiki/Machine_learning')
article.download()
article.parse()
article.nlp()
corpus=article.text
#print
#print(corpus)

text=corpus
sent_tokens=nltk.sent_tokenize(text)
#print(sent_tokens)

#remove_punct_dict=dict( (ord(punct),None) for punct in string.punctuation)  #storing all the punctuations
#print(string.punctuation)
#print(remove_punct_dict)

def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))  #all the words are in lower case
#print(LemNormalize(text))

greeting_input=["hi","hello","hey","hola"]  #keywords for greetings
greeting_response=["howdy","hey there","hi","hello :)"]
def greeting(sentence):
  for word in sentence.split():
    if word.lower() in greeting_input:
      return random.choice(greeting_response)

def response(user_response):
 #user response and robo responce
  #user_response="WHat is chronic disease"
  user_response=user_response.lower()
  #print(user_response)
  #robo response
  robo_response=''
  sent_tokens.append(user_response)
  #print(sent_tokens)
  tfidfvec=TfidfVectorizer(tokenizer=LemNormalize , stop_words='english')
  tfidf=tfidfvec.fit_transform(sent_tokens)
  #print(tfidf)
  #get similarity score
  val=cosine_similarity(tfidf[-1],tfidf)
  #print(val)
  idx=val.argsort()[0][-2]
  flat=val.flatten()
  flat.sort()
  score=flat[-2]
  #print(score)
  if score==0:
    robo_response=robo_response+"Sorry,i dont understand"
  else:
    robo_response=robo_response+sent_tokens[idx]

  sent_tokens.remove(user_response)
  return robo_response



greeting_input=["hi","hello","hey","hola","namaste"]
greeting_response=["howdy","hey there","hi","hello :)"]


def greeting(sentence):
  for word in sentence.split():
    if word.lower() in greeting_input:
      return random.choice(greeting_response)
flag=True
print("Hello!!! This is PL Query Chatbot ,I can answer your querys related to machine learning, Type bye to exit")
while(flag==True):
  user_response=input("User:")
  #user_response=user_response.lower()
  if(user_response!='bye'):
    if(user_response=='thanks' or user_response=='thank you'):
      flag=False
      print("PL BOT: anytime :)")
    else:
       if( greeting(user_response) != None):
         print("PL BOT: "+ greeting(user_response))
       else:
         print("PL BOT:"+response(user_response))
  else:
    flag=False
    print("PL BOT: see you later :)")
