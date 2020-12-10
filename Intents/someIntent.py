new_intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi there", "How are you", "Is anyone there?", "Hello", "Good day", "yo", "hey"],
        "responses": ["Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?", "What would you like to know about us?", "Hi, good to see you here. How may I help you?"],
        "context": [""]
    },
    {  
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time", "that's it then"],
        "responses": ["See you!", "Have a nice day", "Bye! Come back again soon.", "If you would like to know more about us just let me know."],
        "context": [""]
    },
    {
        "tag": "thanks",
        "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me", "awesome", "nice",  "appreciate it",  "good call",  "gracias",],
        "responses": ["Happy to help!", "Any time!", "My pleasure", "Glad to help!", "you'r welcome!"],
        "context": [""]
    },
    {
        "tag": "options",
        "patterns": ["How you could help me?", "What you can do?", "What help you provide?", "How you can be helpful?", "What support is offered", "I want help.", "Tell me about yourself", "What do you know?", "help","help me","instructions","huh", "What are you offering.", 'I wanted to ask something', 'what is this', 'what are you'],
        "responses": ["I am a bot designed to help you get more information about our products, contacts, and any other general information about Company.", "I can give you more information about our products, company and contacts."],
        "context": [""]
    },
    {
        "tag":"human",
        "patterns":["How do I talk to a person","I want to talk to a human","how do I call you","I need to speak to a real person","Can you call me","Can I talk to a human","Representative","Speak to a representative","Speak to a Customer service agent","I need to speak to customer service","Can I talk to a representative", 'How can I contact you', 'contact', 'email', 'What is your email', 'webinar'],
        "responses":["yes you can here are our contact details", "here are our contact details", "You can connect with us here."],
        "context": [""]
    },
    {
        'tag':'about',
        'patterns':['Tell me about yourself', 'about Company', 'about', 'about yourself', 'about your company', 'What does your company do?', 'what do you do for living?'],
        "responses":['Null Innovation is a technology company developing products and providing services in the areas of the Internet of Things and Data Science. We are developing products that will help people to accelerate IoT development, make Digital Marketing data smart and monitor vital signs to save a life.'],
        "context":[""]
    },
    {
        'tag':'products',
        'patterns':['products', "Tell me about products.", "What products do you have", "What are you selling?", "What can I buy from you?"],
        "responses":['Here are our products', "these is what we have", "This our product portfolio"],
        "context":[""]
    },
    {
        'tag':'TitanX',
        'patterns':['TitanX', 'about TitanX', 'what is TitanX?', 'what does TitanX do?','I do not know about TitanX','I want to know more about TitanX'],
        "responses":['TitanX analyzes the data coming from Google Analytics, Google Search Console,Social Media Accounts, Email Campaigns and provide you recommendations. As a marketer, it saves you from spending time on data collection, analysis and intelligence extraction; and you can focuse on your core areas'],
        "context":[""]
    },
    {
        'tag':'OzoneX',
        'patterns':['OzoneX', 'about OzoneX', 'what is OzoneX?', 'what does OzoneX do?','I do not know about OzoneX','I want to know more about OzoneX'],
        "responses":['OzoneX is a new generation, wire-less remote patient monitoring system which tracks vital signs - Blood Pressure, Heart Rate, Body Temperature,Blood Oxygen Level,Pulse Rate and can send liva data to remote location'],
        "context":[""]
    },
    {
        'tag':'KeetoX',
        'patterns':['KeetoX', 'about FramGen', 'what is KeetoX?', 'what does KeetoX do?','I do not know about KeetoX','I want to know more about KeetoX'],
        "responses":['KeetoX is a Software that generates framework for IoT development. Use KeetoX to create entire framework before you touch your hardwares. It includes Hardware, Device Software, Communication, Cloud, Securtiy, Compliances'],
        "context":[""]
    },
    {
        'tag':'Service',
        'patterns':['Do you provide any services?', 'about Service', 'What kind of services are you offering?', 'what about services?','I want to automate my digital services','Do you take work?'],
        "responses":['Currently, we are not providing any services. However check our product portfolio if something helps you'],
        "context":[""]
    },
    {
        'tag':'TitanX_Price',
        'patterns':['How much TitanX cost?', 'What are pricing plans for TitanX', 'pricing of TitanX?', 'Subscription plan for TitanX?','How much TitanX cost?','I want to buy TitanX?','How can I buy TitanX', 'TitanX price', 'cost of TitanX', 'TitanX cost'],
        "responses":['TitanX Beta is available free of charge rightnow. Just sign up and Enjoy. Sign Up Here: Link'],
        "context":[""]
    },
    {
        'tag':'OzoneX_Price',
        'patterns':['How much OzoneX cost?', 'What are pricing plans for OzoneX?', 'pricing of OzoneX?', 'Subscription plan for OzoneX?','How much OzoneX cost?','I want to buy OzoneX','How can I buy OzoneX', 'OzoneX price',  'cost of OzoneX', 'OzoneX cost'],
        "responses":['OzoneX pricing plan is coming up. Please leave your email and name, we will reach out to you. Link:Form'],
        "context":[""]
    },
    {
        'tag':'KeetoX_Price',
        'patterns':['How much KeetoX cost?', 'What are pricing plans for KeetoX?', 'pricing of KeetoX?', 'Subscription plan for KeetoX?','How much KeetoX cost?','I want to buy KeetoX?','How can I buy KeetoX', 'KeetoX price', 'cost of KeetoX', 'KeetoX cost' ],
        "responses":['TitanX is available free of charge. Just sign up and Enjoy. Sign Up Here Link:'],
        "context":[""]
    },
    {
        'tag':'Availabiity',
        'patterns':['Is it available in my country?', 'Can I pay in dollar?', 'my counytry is India,is it available here?', 'Subscription plan for TitanX?','How much TitanX cost?','I want to buy TitanX?','How can I buy TitanX', 'TitanX price'],
        "responses":['TitanX is available in English Langauage right now. You can pay in Dollar, Euro and INR.'],
        "context":[""]
    },
    {
        'tag': 'ok',
        'patterns': ['ok', 'What else?', 'hm..', 'I get it now', 'cool', 'nice', 'okay'],
        'responses':['was it helpful?', 'did it help?'],
        'context':['']
    },
    {
        'tag': 'yes',
        'patterns':['yes', 'of course', 'yah'],
        'responses':['Glad to hear that. What else would you like to know?', ':) what else would you like to know'],
        'context':['']
    },
    {
        'tag': 'no',
        'patterns':['no', 'nah', 'nop', 'thats not helping', 'did not help', '?', 'I dont understand'],
        'responses':['sorry to hear that, you can try framing your questions differently. I will try to improve myself next time.'],
        'context':['']
    },
    {
        'tag': 'ask',
        'patterns':['can I ask you something', 'I had some doubts', 'I have questions', 'I wanted to ask something', 'i wanted some intel', 'i want information', 'i want to know more'],
        'responses':['I am a bot designed to help you get information about our services and products, go ahead and ask me anything, I will be glad to help you'],
        'context':['']
    },
    {
        'tag': 'angry',
        'patterns': ['I hate you', 'I want refund!', '!!', 'this is waste of time', 'stupid', 'this bot is useless', 'Why is this thing so difficult to understand', 'bot is broken'],
        'responses': ['oops', 'peepee poopoo', 'nobody cares actually'],
        'context':['']
    }
]