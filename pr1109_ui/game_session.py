import mqtt
import json
import random

class GameSession:
    def __init__(self, callback = None, context = None):
        mqtt.connect(GameSession.onMsg, self)
        self.id = random.randint(1, 1000000000)
        # self.id = random.randint(1, 10)
        print("I am:", self.id)
        self.wants = False
        self.callback = callback
        self.context = context
        self.opponent = 0
    def close(self):
        if self.opponent != 0:
            mqtt.publish(json.dumps({'cmd':'clo','from':self.id,'to':self.opponent}))
        mqtt.disconnect()

    def send(self, message):
        if self.opponent == 0:
            print("I don't have any opponent")
            return
        msg = {'cmd':'msg','to':self.opponent,'body':message}
        mqtt.publish(json.dumps(msg))

    @staticmethod
    def onMsg(msg, self):
        print('msg', msg)
        dict = json.loads(msg)
        print('dict', dict)
        if 'cmd' in dict:
            cmd = dict['cmd']
            if cmd == 'want':
                self.onWant(dict['id'])
            elif cmd == 'est':
                self.onEstablished(dict['from'], dict['to'])
            elif cmd == 'msg':
                if dict['to'] != self.id:
                    print("Not a message for me")
                    return
                if self.callback == None:
                    print("No callback is assigned. Ignoring.")
                    return
                cb = self.callback
                print("cb:", cb)
                cb(dict['body'], self.context)
            elif cmd == 'clo':
                self.opponent = 0

    def onWant(self, id):
        if not self.wants:
            print("Now I don't want to connect:", id)
            return
        if id == self.id:
            print("I's me. Ignoring")
            return
        self.opponent = id
        self.wants = False
        msg = {'cmd':'est','from':self.id,'to':id}
        mqtt.publish(json.dumps(msg))
    def onEstablished(self, fromId, toId):
        if not self.wants:
            print("I'm not in the mood:", fromId, "->", toId)
            return
        if toId != self.id:
            print("To is not me:", self.id, " <> ", toId)
            return
        self.opponent = fromId
        self.wants = False
        print("Established")

    def wantGame(self, wants):
        self.wants = wants
        if wants:
            msg = {'cmd':'want','id':self.id}
            mqtt.publish(json.dumps(msg))