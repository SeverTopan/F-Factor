import json
import logging
from channels import Group
from channels.sessions import channel_session
from django.db.models import F
from django.db import transaction
from leaderboard.models import Entry


log = logging.getLogger(__name__)
GROUP_NAME = 'leaderboard'

@channel_session
def ws_connect(message):
    print("connection obtained")
    Group(GROUP_NAME).add(message.reply_channel)
    message.reply_channel.send({"accept": True})

@channel_session
def ws_receive(message):
    print("recieve obtained")
    
    # load and scrub input
    try:
        data = json.loads(message['text'])
    except ValueError:
        print("ws message isn't json text=%s", message['text'])
        return
    
    if set(data.keys()) != set(('name', 'direction')):
        print("ws message unexpected format data=%s", data)
        return

    # check if data
    if not data:
        return

    # update object
    print('chat message name=%s direction=%s', data['name'], data['direction'])
    print(Entry.objects.all().values_list('name', flat=True))

    try:
        with transaction.atomic():
            entry = Entry.objects.get(name=data['name'])

            if data['direction'] == 'increment':
                entry.real_score += 1
            elif data['direction'] == 'decrement':
                entry.real_score -= 1
            else:
                print("unknown direction=%s", data['direction'])
                return

            entry.save()

    except Entry.DoesNotExist:
        log.debug('recieved message, but entry does not exist')
        return
    except:
        log.debug('an error occurred')
        return

    # Need to be explicit about the channel layer so that testability works
    Group(GROUP_NAME).send({'text': json.dumps(entry.as_dict())})

@channel_session
def ws_disconnect(message):
    print("disconnect obtained")
    Group(GROUP_NAME).discard(message.reply_channel)
