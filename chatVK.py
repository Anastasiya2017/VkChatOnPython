import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token = '')
session_api = session.get_api()
longpoll = VkLongPoll(session)

hello_list = ('И тебе привет!',
              'Hello!',
              'Здравствуйте!')

films_list = ('Хатико',
              'Один дома',
              'Пираты Карибского моря',
              'Один + один')

img_list = ('photo-31466113_457435534',
              'photo-31466113_457435549',
              'photo-31466113_457435550',
              'photo-31466113_457435525')

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ', event.datetime)
            print('Текст сообщения: ', event.text)
            response = event.text.lower()
            if event.from_user and not event.from_me:
                    if response.find('привет') >= 0 or response.find('здравств') >= 0:
                        time.sleep(random.uniform(0.5,3.0))
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message': random.choice(hello_list),
                                        'random_id':'0'})
                    elif response.find('как дела') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message': '',
                                        'random_id':'0',
                                        'sticker_id': '14997'})

                    elif response.find('фильм') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message': random.choice(films_list),
                                        'random_id':'0'})
                        
                    elif response.find('картин') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message': '',
                                        'random_id':'0',
                                        'attachment': random.choice(img_list)})
                    
                    else: session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message': 'Анастасия пока не может ответить на Ваше сообщение. Она отвечает всегда, но не всегда сразу))',
                                        'random_id':'0'})
                        
