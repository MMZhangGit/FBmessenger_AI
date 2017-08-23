from wit import Wit
# from gnewsclient import gnewsclient
access_token = "YY3Q7GSQ7NIFBWKUGHMU2ASYJDPUMX5U"
client = Wit(access_token=access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    # categories = {'newstype': None, 'location': None}
    # categories = {'intent_v': None, ' confidence': 0 }
    categories = {}
    if not resp.get('entities'):
        return categories
    entity = list(resp['entities'])[0]
    try:
        categories['intent_v'] = resp['entities'][entity][0]['value']
        categories['confidence'] = resp['entities'][entity][0]['confidence']
    except:
        categories['intent_v'] = None
        categories['confidence'] = 0
    # value = resp['entities'][entity][0]['value']
    # confidence = resp['entities'][entity][0]['confidence']


    # entities = list(resp['entities'])
    # for entity in entities:
    #     categories[entity] = resp['entities'][entity][0]['value']

    return categories


# def get_news_elements(categories):
#     news_client = gnewsclient()
#     news_client.query = ''
#
#     if categories['newstype'] != None:
#         news_client.query += categories['newstype'] + ' '
#
#     if categories['location'] != None:
#         news_client.query += categories['location']
#
#     news_items = news_client.get_news()
#
#     elements = []
#
#     for item in news_items:
#         element = {
#             'title': item['title'],
#             'buttons': [{
#                 'type': 'web_url',
#                 'title': "Read more",
#                 'url': item['link']
#             }],
#             'image_url': item['img']
#         }
#         elements.append(element)
#
#     return elements

# from wit import Wit
# access_token = "YY3Q7GSQ7NIFBWKUGHMU2ASYJDPUMX5U"
# client = Wit(access_token = access_token)
# def wit_response(message_text):
#     resp = client.message(message_text)
#     entity = None
#     value = None
#     confidence = 0
#     try:
#         entity = list(resp['entities'])[0]
#         value = resp['entities'][entity][0]['value']
#         confidence = resp['entities'][entity][0]['confidence']
#     except:
#         pass
#     if value == "major":
#         print("my major is:")
#     else:
#         print("empty")
#     return (entity, value)

# message_text = "where are you from?"
# resp = client.message(message_text)
# print(resp)
# print(wit_response("where are you from?"))
# resp = wit_response("what's your major?")
# print(resp[1])