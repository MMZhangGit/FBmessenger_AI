import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger.bot import Bot

# create the application
app = Flask(__name__)
# Facebook Page Access Token
ACCESS_TOKEN = "EAAbRzQm2QUEBAD6Cdb3uF5Lv2vKpKCKTIF6jwG8N7WX4eEOSk0GHcCpG7rFysFiL2LgmtD3v8MypZAXIF2ulDNxG1a1yRbZAZB1X6xMsfAuj58I5WU9tiWH283vZAv4GRaT7lRTClLPMHx1k4sr7Dy4s9QuGXLzTKLIroliQEwZDZD"
VERIFY_TOKEN = "hello" # verify token for webhook
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        # At your webhook URL, add code for verification.
        # Your code should look for the Verify Token and respond with the challenge sent in the verification request.
        # Click Verify and Save in the New Page Subscription to call your webhook with a GET request.
        if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
            if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
                return "Verification token mismatch", 403
            return request.args["hub.challenge"], 200
        return "Hello world", 200

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        categories = wit_response(message)
                        if categories.get('confidence') and categories['confidence'] > 0.75:
                            rp_message = ''
                            if categories['intent_v'] == 'major':
                                rp_message = "My major is Electrical & Computer Engineering"
                            elif categories['intent_v'] == 'name':
                                rp_message = "My name is Min"
                            elif categories['intent_v'] == 'college':
                                rp_message = "I graduated from Old Dominion University"
                            elif categories['intent_v'] == 'place_from':
                                rp_message = "I'm from China"
                            elif categories['intent_v'] == 'place_growup':
                                rp_message = "I grew up in a small town in China"
                            elif categories['intent_v'] == 'fav_class':
                                rp_message = "My favorite classes include Machine Learning, Algorithm, and Statistics."
                            elif categories['intent_v'] == 'greeting':
                                rp_message = "Hello, my name is Min. How can I help you?"
                            elif categories['intent_v'] == 'fav_program_lan':
                                rp_message = "If I do have to pick a favorite one, it would either be C/C++, python, or C# depending on the kind of project, as I have used these the most. But I won't hesitate to use other languages if those will do a better job. I like C++, because it is fast, precise, and reasonably close to machine language as far as high level languages go. I also like Python because it is very easy to use."
                            elif categories['intent_v'] == 'best_at_program_lan':
                                rp_message = "I am good at more than one language. If I do have to pick one, it would either be C/C++, python, or C# depending on the kind of project, as I have used these the most."
                            elif categories['intent_v'] == 'time_learn_program':
                                rp_message = "I started to learn programming in my first year of undergrad, that was 10 years ago."
                            else:
                                rp_message = 'I am sorry, I could not understand what you are asking.'
                            bot.send_text_message(recipient_id, rp_message)
                        else:
                            message = 'I am sorry, I could not understand what you are asking.'
                            bot.send_text_message(recipient_id, message)
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5000, debug=True)

