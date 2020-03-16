# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:27:49 2020

@author: hp
"""

#  Importing Classes

from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"(my|My) name is (.*)",
        ["Hello %1, How are you today?",]
    ],
     [
        r"(what|What) is your name?",
        ["My name is Scotty and I'm a chatbot?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. \n How about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"Hi|Hey|Hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program. \n Seriously you are asking me this?",]
        
    ],
    [
        r"(What|what) (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) (created|creator) ?",
        ["Nithin created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Mumbai, India',]
    ],
    [
        r"(how|How) is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"(I|i) work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"(how|How) (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"(who|Who) (.*) sportsperson ?",
        ["Lionel Messi","Christiano Ronaldo","Wayne Rooney"]
],
    [
        r"(who|Who) (.*) (moviestar|actor)?",
        ["Tom Cruise"]
],
    [
        r"quit|Quit",
        ["Bye!! Take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

services= [
        [
                r"Hi|Hey|Hello",
                ["Hello, My name is Scotty and I'm a chatbot. How I can I serve you?", "Hey there, I am Scotty, the coolest chatbot in the world, here to assist you."] 
        ],
        [
                r"(.*) describe company",
                ["Hoppoo Lifestyle India Pvt. Ltd. is a multi-services company who strives to provide customers quality solutions at affordable prices"]
        ],
        [
                r"(.*) your services",
                ["We provide the following services : My Rides, Journey Anywhere, Grocery, Entertainment, Education, Insurance, IT & Corporate Services"]
        ],
        [
                r"(.*) My Rides",
                ["This service is for people who travel a lot and are looking to reduce their travelling costs. You can get Rs.12000 worth travel at just Rs.7999"]
        ],
        [
                r"(.*) Grocery",
                ["Grocery is an ever present and significant expense in every household. You can buy Rs.18000 worth grocery at just Rs. 13999."]
        ],
        [
                r"(.*) Entertainment",
                ["This service is for movie lovers. You can watch a movie every week @ just Rs. 5999."]
        ],
        [
                r"(.*) Journey Anywhere",
                ["For those who love to travel, you can get 6 train tickets and 6 bus tickets at just Rs. 29999."]
        ],
        [
                r"any other (.*)",
                ["We also provide travel packages to many vacation destinations. For more details, you can contact us directly."]
        ],
        [
        r"quit",
        ["Bye!! Take care. See you soon :) ","It was nice talking to you. See you soon :)"]
        ],
        ]

def scotty():
        print("Hi, I'm Scotty and I chat alot ;) \n Type quit to leave ") #default message at the start
        chat = Chat(services, reflections)
        chat.converse()
if __name__ == "__main__":
    scotty()
    
    