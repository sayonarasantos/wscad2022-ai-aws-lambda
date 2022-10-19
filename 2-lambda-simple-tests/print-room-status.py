import json


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

# def lambda_handler(event, context):
#     message = f"Room status -- Temperature: {event['temperature']}; " \
#               f"Humidity: {event['humidity']}; Light: {event['light']}."

#     return {
#         'message': message
#     }
