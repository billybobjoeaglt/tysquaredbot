import StringIO
import json
import logging
import random
import urllib
import urllib2
import random
import time

p = ["A recent study has found that women who carry a little extra weight live longer than the men who mention it.",
"Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.",
"I changed my password to 'incorrect'. So whenever I forget what it is the computer will say 'Your password is incorrect'.",
"Apparently taking a day off is not something you should do when you work for a calendar company.",
"I heard Apple is designing a new automatic car. But they're having trouble installing windows.",
"I wonder how letters ever get to the recipient. The envelopes, afterall, are stationery.",
"Just found the worst page in the entire dictionary. What I saw was disgraceful, disgusting, dishonest, and disingenuous.",
"I totally understand how batteries feel because I'm rarely ever included in things either.",
"My friend recently got crushed by a pile of books, but he’s only got his shelf to blame.",
"Time flies like an arrow, fruit flies like banana.",
"I knew a guy who collected candy canes, they were all in mint condition.",
"Never discuss infinity with a mathematician, they can go on about it forever.",
"The only thing in common between a stork and an obstetrician is the long bill.",
"I'm competing for that stair climbing competition. Guess I better step up my game.",
"The plane flight brought my acrophobia to new heights.",
"I can never understand my trigonometry teacher because he always talks in sine language.",
"The deer population is staggering.",
"Did you hear about the computer technician who received third degree burns? He touched the firewall.",
"Stairs are useful and all, but elevators are really some next level technology.",
"The Environmental Committee held a meeting on Saturday. They decided that we need to cut down on deforestation.",
"A pessimist's blood type is always b-negative.",
"I tinted my hair today. It was the highlight of my day.",
"I felt super exhausted after giving blood. It's such a draining procedure.",
"I'd tell you a chemistry joke but I know I wouldn't get a reaction.",
"My first job was working in an orange juice factory, but I got canned: couldn't concentrate.",
"I wasn't originally going to get a brain transplant, but then I changed my mind.",
"I'm reading a book about anti-gravity. It's impossible to put down."]

d = ["That's a crooked tree. We'll send him to Washington.",
"I like to beat the brush.",
"In painting, you have unlimited power. You have the ability to move mountains. You can bend rivers. But when I get home, the only thing I have power over is the garbage.",
"You need the dark in order to show the light.",
"Look around. Look at what we have. Beauty is everywhere—you only have to look to see it.",
"Just go out and talk to a tree. Make friends with it.",
"There's nothing wrong with having a tree as a friend.",
"Trees cover up a multitude of sins.",
"They say everything looks better with odd numbers of things. But sometimes I put even numbers—just to upset the critics.",
"How do you make a round circle with a square knife? That’s your challenge for the day.",
"I remember when my Dad told me as a kid, ‘If you want to catch a rabbit, stand behind a tree and make a noise like a carrot. Then when the rabbit comes by you grab him.",
"We tell people sometimes: we're like drug dealers, come into town and get everybody absolutely addicted to painting. It doesn't take much to get you addicted",
"The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe",
"Water's like me. It's laaazy ... Boy, it always looks for the easiest way to do things",
"I really believe that if you practice enough you could paint the 'Mona Lisa' with a two-inch brush.",
"If I paint something, I don't want to have to explain what it is",
"We don't make mistakes. We just have happy accidents.",
"The stream can go whatever way you want, it's your little stream",
"Happy Little Cloud",
"Happy Little Trees",
"Sneaky little cloud! Running around here at night",
"Brown snow is worse than yellow snow",
"and maybe there's a little cloud over here, just a little floater.",
"Sometimes you have to scare em out, scare those little rascals out",
"The little trees are just there, hiding in your brush and you have to find them",
"I don't want you to be unhappy', 'Everything in nature is pretty... use it!",
"All you need is a dream in your heart', 'That'll be our little secret.",
"Gotta give him a friend. Like I always say 'everyone needs a friend'.",
"We don't know where it goes. We don't really care.",
"Any time ya learn, ya gain.",
"Be sure to use odorless paint-thinner. If it's not odorless, you'll find yourself working alone very, very quick.",
"Clouds are very, very free.",
"Tender as a mothers love... And with my mother, that was certainly true.",
"Just scrape in a few indications of sticks and twigs and other little things in there. People will think you spend hours doing this.",
"Maybe in our world there lives a happy little tree over there.",
"Oh, that would make a nice place to fish. I like fishing, but I'm not a very good fisherman. I always throw the fish back into the water, just put a band-aid on his mouth, tap 'im on the patootie and let him on his way. And maybe some day, if I'm lucky, I'll get to catch him again.",
"Shwooop. Hehe. You have to make those little noises, or it just doesn't work.",
"People look at me like I'm a little strange, when I go around talking to squirrels and rabbits and stuff. That's ok. Thaaaat's just ok.",
"Try to imagine that you are a tree. How do you want to look out here?",
"We want happy paintings. Happy paintings. If you want sad things, watch the news.",
"We're gonna make some big decisions in our little world.",
"From all of us here I'd like to wish you happy painting...and God bless you my friend.",
"And just go straight in like your going to stab it. And barely touch it...barely touch it.",
"This old barn has seen it's better days, it's like me... it's had a rough life",
"when life gives you lemons, complain that you didn't also get sugar and water, because just lemons makes for shitty lemonade"]
# for sending images
from PIL import Image
import multipart

countries = ['VENEZUELA', 'CANADA']
# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = '212113093:AAFuDScHj91KvuNVB4YLPENaxZkguNkcxAY'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)

        if text.startswith(''):
            if text == '/start':
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif text == '/stop':
                reply('Bot disabled')
                setEnabled(chat_id, False)
            elif text == '/imag':
                #img = 'https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg'
                #base = random.randint(0, 16777216)
                #pixels = [base+i*j for i in range(512) for j in range(512)]  # generate sample image
                #img.putdata(pixels)
                #output = StringIO.StringIO()
                #img.save(output, 'JPEG')
                reply()
            elif text == '/ping' or text == '/ping@tysquaredbot':
                reply('pong')
            elif text == '/wisdom' or text == '/wisdom@tysquaredbot':
                reply(random.choice(d))
            elif text == '/bob':
                reply(random.choice(countries))
            elif text == '/cat':
                reply()
            elif text == '/pun' or text == '/pun@tysquaredbot':
                reply(random.choice(p))
            elif text == '/pun@automod_bot':
                reply(random.choice(p))
            elif text == '/viraj' or text == '/viraj@tysquaredbot' or text == 'Viraj':
                reply('garaje')
            elif text == 'viraj':
                reply('garaje')
            else:
                reply()

        elif 'who are you' in text:
            reply('telebot starter kit, created by tyty')
        elif 'what time' in text:
            reply('look at the corner of your screen!')
        else:
            if getEnabled(chat_id):
                #reply('I got your message! (but I do not know how to answer)')
                reply()
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
