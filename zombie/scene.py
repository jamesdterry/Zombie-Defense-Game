#
# Scene
#

class Scene:
    game = None
    s = None

    def __init__(self, game):
        self.game = game
        self.s = game.s
        print "Init Scene " + self.__class__.__name__

    def load(self):
        pass

    def cleanup(self):
        pass

    def do_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass
