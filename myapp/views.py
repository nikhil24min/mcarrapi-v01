from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework import permissions

import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a robo receptionist created by iot group.",]
    ],
    [
        r"mca lab|where is mca lab",
        ["mca lab is in central block, 8th floor, room number 811",]
    ],
    [
        r"tell me about mca|may i know about mca",
        ["mca is Master fo computer applications program offered by the Christ deemed to be university. It is a professional course and is spread over a time of 2 years.",]
    ],
    [
        r"what are the courses in computer science|courses in computer science|course",
        ["Undergraduate Programmes are BSc CME, BSc in CMS, BCA. Postgraduate Programmes MSc Cs, Msc CS and Applications, MCA. Research Programmes Phd.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good and How about You ?",]
    ],
    [
        r"(.*)deepa(.*)",
        ["Dr deepa v jose is an assistant professor in computer science department. she has done MCA, MTech, MPhil, PhD",]
    ],
    [
        r"(.*)senthilnathan(.*)",
        ["Dr senthilnathan is an associate professor in computer science department. she has done MCA, ME, MPhil, PhD",]
    ],
    [
        r"(.*)chandra(.*)",
        ["Dr chandra J is an assistant professor in computer science department. she has done MCA, MPhil, PhD",]
    ],
    [
        r"(.*)teachers|faculty(.*)",
        ["Dr Deepa V Jose, Dr Chandra J, Dr senthilnathan, Dr Sagaya Aurelia, Dr Shoney Sebastian",]
    ],
    [
        r"sorry(.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"where should i enquire about mca admissions| admissions",
        ["You can get admission details in Christ University website or visit central block 0th floor admission office",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["IOT group created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Analytics Vidhya for your service")
    chat = Chat(pairs, reflections)
    # chat.converse()

    print(chat.respond("MCA"))

def getreply_func(data):
    resultdata = data * data
    return resultdata

# Create your views here.
class replyapplist(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        print(request)
        result = getreply_func(4)
        return Response({'result':result}, status=status.HTTP_200_OK)
    
    
    
class replyapp(APIView):
    def get(self, request, query, *args, **kwargs):
        chat = Chat(pairs, reflections)
        print(query)
        result = chat.respond(query)
        print(result)
        return JsonResponse(result,status=status.HTTP_200_OK, safe=False)
        return Response({'result':result}, status=status.HTTP_200_OK)
