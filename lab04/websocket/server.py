import random 
import tornado.ioloop
import tornado.web
import tornado.websocket

class websocket(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        WebSocketServer.clients.add(self)

    def on_close(self):
        WebSocketServer.clients.remove(self)
        
    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message to {len(cls.clients)} clients(s).")
        for clietn in cls.clients:
            client.write_message(message)
            
class randomWordSelector:
    def __init__(self, words):
        self.words = words
    
    def sample(self):
        return random.choice(self.words)
    
    def main():
        app = tornado.web.Application(
            [(r"/websocket/", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )
        app.listen(8080)
        
        io_loop = tornado.ioloop.IOLoop.current()
        
        word_selector = randomWordSelector(["apple", "banana", "cherry", "oragne","grape",])
        
        periodic_callback = tornado.ioloop.PeriodicCallback(
            lambda: WebSocketServer.send_message(word_selector.sample()),
            1000,
        )
        periodic_callback.start()
        
        io_loop.start()
        
        if __name__ == "__main__":
            main()