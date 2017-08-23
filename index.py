import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = "EAAbRzQm2QUEBAMAfmQTaIZAQ61rSP4eKKTfpv0We5P8DgA3QHdz2F0mJgLtCffdQ8gmGDk2iacryRwUVpjJfewZCdnWkgPTj0wjrHfNHpQ2MtGuSTuMLGZBpzRSM4URZB21C2AYCyMslxCbNupKsHRdVdfZB0222qEE0sUSBAvwZDZD"
VERIFY_TOKEN = "hello"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
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
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)

# import os, sys
# from flask import Flask, request
# from pymessenger import Bot
#
# app = Flask(__name__)
#
# PAGE_ACCESS_TOKEN = "EAAbRzQm2QUEBAJ5y36eQGSgS4HOqz9MMw8KD921qwIZBRODBgOZA7KMzGtFMeIdsR8Ehq0vRpT20MtoslrKe0SpPwc5snSmUDGsoujqdGB1I9YDYUCDMdtlR96HZCo7KkK8o1EAskmK97bLPMzUZBxbsflnjbpwf1Pb3vC7b7gZDZD"
#
# bot = Bot(PAGE_ACCESS_TOKEN)
#
#
# @app.route('/', methods=['GET'])
# def verify():
#     # Webhook verification
#     if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#         if not request.args.get("hub.verify_token") == "hello":
#             return "Verification token mismatch", 403
#         return request.args["hub.challenge"], 200
#     return "Hello world", 200
#
#
# @app.route('/', methods=['POST'])
# def webhook():
#     data = request.get_json()
#     log(data)
#
#     if data['object'] == 'page':
#         for entry in data['entry']:
#             for messaging_event in entry['messaging']:
#
#                 # IDs
#                 sender_id = messaging_event['sender']['id']
#                 recipient_id = messaging_event['recipient']['id']
#
#                 if messaging_event.get('message'):
#                     # Extracting text message
#                     if 'text' in messaging_event['message']:
#                         messaging_text = messaging_event['message']['text']
#                     else:
#                         messaging_text = 'no text'
#                     # Echo
#                     response = messaging_text
#                     bot.send_text_message(sender_id, response)
#                     # response = 'message for testing'
#                     # bot.send_text_message(sender_id, response)
#                 # response = 'message for testing'
#                 # bot.send_generic_message(sender_id, response)
#     return "ok", 200
#
#
# def log(message):
#     print(message)
#     sys.stdout.flush()
#
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5002)
#
#     # from flask import Flask, request
#     # # from utils import wit_response
#     #     # get_news_elements
#     # # from pymessenger import Bot
#     #
#     # app = Flask(__name__)
#     #
#     # # test code
#     # @app.route('/')
#     # def index():
#     # 	return '<h1>Deployed to Heroku!!</h1>'
