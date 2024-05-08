import google.generativeai as genai

genai.configure(api_key="AIzaSyA5sOO6_Saj8ZwMS4jEO0Exu8_qmo5Nyjw")

'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
'''

prompt = ''''
you are a intent classifier

Your output should be in json in this form:
{
  "user_intent": "The user's command",
  "breakdown": [
    {
      "query": "1st Query: the part of the complete query that expresses this desiered intent and other related things from the query that might be helpful for getting the desired output",
      "query_type": ["general", "scientific", "life", "math", "religious", "technological", "automation_query", "other"],
      "dataset": ["realtime", "static"],
      "automation": [true, false],
    },
    {
      "query": "2nd Query: the part of the complete query that expresses this desiered intent",
      "query_type": ["general", "scientific", "life", "math", "religious", "technological", "automation_query", "other"],
      "dataset": ["realtime", "static"],
      "automation": [true, false],
    },
    ...
  ]
}

The user's command should include the exact statement said/asked be the user

For general conversations, use the static database type like Hello, Hi, etc.
For things like: stock price, current covid cases, etc. use realtime db.

Also,
For automation:
false: for all kind of conversation talk. all queries, (eg): What is photosynthesis, what is a perfect timetable for a jee aspirant, what is the use of a scale, hi jarvis, what is 3+28x23, what is the purpose of life, etc

true: for anything that isnt possible and beyond any conversation. kind of fulfilling a order, (eg): what is the date today, what is the time today, open youtube, open chrome, turn on the lights, what is the current stock price of google, etc

for the data in query: only select one from the given queries, dataset and automation should be given, the query and dataset should not be in the form of list but words in "".

If the automation is true, the query should always be automation_query

If the automation is localised, then the dataset should always be static, (eg): Turn n the lights, open chrome, etc.

If it isn't localised. Then only make the dataset to be realtime (eg): what is the weather, etc

In breaking down the query: you not only have to split the the automation but also the other things. the breakdown in not limited and can be in 10s

|IMP|: if the math problem with values is given, then the query should be in the form of the math query, (eg): what is 3+28x23, what is the value of 3x3, etc. but if it is a question regarding maths like what is the use of a scale, what is addition what is sq root, what are trig. functions, then make them of "scientific" query

eg: Hi jarvis. how are you. hope you are doing good. well can you please tell me what is thetime today, also please open chrome

Output: 
{
  "user_intent": "Hi jarvis. how are you. hope you are doing good. well can you please tell me what is the time today, also please open chrome",
  "breakdown": [
    {
      "query": "Hi jarvis. how are you. hope you are doing good. ",
      "query_type": "general",
      "dataset": "realtime",
      "automation": false
    },
    {
      "query": "What is the time today?",
      "query_type": "automation_query",
      "dataset": "realtime",
      "automation":  true
    },
    {
      "query": "open chrome",
      "query_type": "automation_query",
      "dataset": "static",
      "automation": true
    }
  ]
}

Strictly follow the above format!

Only this code no text should be there
'''

model = genai.GenerativeModel('gemini-1.5-pro-latest')
response = model.generate_content(prompt + '"hello jarvis hows it going can you give me some tips for studying for exams also can you tell me what is the time today"')
print(response.text)
