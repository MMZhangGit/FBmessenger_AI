from wit import Wit
access_token = "YY3Q7GSQ7NIFBWKUGHMU2ASYJDPUMX5U"
client = Wit(access_token=access_token)

def wit_response(message_text):
    resp = client.message(message_text)
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
    return categories
