from fastapi import FastAPI #importing the FastAPI class from the fastapi module
import random #importing the random module to generate random side hustles and money qoutes

#creating an instance of the FastAPI class
app =FastAPI()

#list of side hustles for the side hustles endpoint
side_hustles = ["Start a freelance writing business",
    "Create and sell online courses",
    "Become a virtual assistant",
    "Start a dropshipping business",
    "Offer social media management services",
    "Create and sell digital products",
    "Start a web development business",
    "Become an online tutor",
    "Start a photography business",
    "Create and monetize a blog",
    "Offer graphic design services",
    "Start a podcast",
    "Become an affiliate marketer",
    "Create and sell printables",
    "Start a YouTube channel",
    "Offer consulting services",
    "Start an e-commerce store",
    "Become a translator",
    "Offer video editing services",
    "Start a mobile app development business"
]

#list of side money for the side money endpoint
money_qoutes = ["Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going. ",
    "Believe you can and you're halfway there. ",
    "It always seems impossible until it's done.",
    "Khudi ko kar buland itna ke har taqdeer se pehle, khuda bande se khud pooche, 'Bata teri raza kya hai?'" ,
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
"Great things never come from comfort zones.",
"Dream it. Wish it. Do it.",
"Success doesn't just find you. You have to go out and get it.",
"The harder you work for something, the greater you'll feel when you achieve it.",
"Don't stop when you're tired. Stop when you're done.",
"Wake up with determination. Go to bed with satisfaction.",
"Do something today that your future self will thank you for.",
"Little things make big days.",
"It’s going to be hard, but hard does not mean impossible.",
"Don't wait for opportunity. Create it.",
"Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
"The key to success is to focus on goals, not obstacles.",
"Your only limit is you.",
"people who are crazy enough to think they can change the world",
"Success is not how high you have climbed, but how you make a positive difference to the world.",
"people who are crazy enough to think they can change the world. – Steve Jobs",
"Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
"wake up with determination, go to bed with satisfaction",
"make each day your masterpiece",
"the only limit to our realization of tomorrow will be our doubts of today",
"the only way to do great work is to love what you do",
"the only way to achieve the impossible is to believe it is possible",
"a dream doesn't become reality through magic; it takes sweat, determination, and hard work",
"coding opens up a world of possibilities",
"never give up on a dream just because of the time it will take to accomplish it. the time will pass anyway"
'rich people have small tvs and big libraries, and poor people have small libraries and big tvs',
"the only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it",
"success is not about being the best, it's about being better than you were yesterday",
"money is only a tool, but it's a tool that can help you achieve your dreams",
"invest in yourself, it pays the best interest",
"your time is limited, don't waste it living someone else's life",
"wealth is not about having a lot of money, it's about having a lot of options",
"the greatest wealth is to live content with little",
"don't tell me what you value, show me your budget and I'll tell you what you value",
"financial freedom is about much more than just having money",
"money makes your life easier. If you're lucky to have it, you're lucky",
"every day is a bank account, and time is our currency"
]


#defining the route for the side hustles endpoint
@app.get("/side_hustles") #Get decorator for the side hustles endpoint & /side_hustles for the route handler
def  get_side_hustles():
    """Returns a random side hustle idea""" #docstring for the function 
    return {"side_hustle": random.choice(side_hustles)} #returning a random side hustle from the list of side hustles


#defining the route for the side money endpoint
@app.get("/money_qoutes") #Get decorator for the side money endpoint & /money_qoutes for the route handler
def  get_money_qoutes():
    """Returns a random money qoute""" #docstring for the function
    return {"money_qoute": random.choice(money_qoutes)} #returning a random money qoute from the list of money qoutes





    