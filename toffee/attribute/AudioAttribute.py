from toffee.attribute.Attribute import Attribute


class AudioAttribute(Attribute):
    def __init__(self):
        self.audio = None

    def construct(self, src, volume, node):
        self.audio = base.loadSfx(src)
        base.playSfx(self.audio, volume=volume, node=node, looping=True)

    def destroy(self):
        self.audio.stop()
