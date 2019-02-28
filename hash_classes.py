
class Image(object):
    def __init__(self, id, orientation, tags):
        self.id = id
        # image orientation
        self.orientation = orientation
        # images tags
        self.tags = tags
        # length of tags
        self.M = len(tags)

class Slide(object):
    def __init__(self, images):
        self.images = images
        self.M = len(images)
