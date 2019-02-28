
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
        if len(images) > 1:
            if images[0].orientation != images[1].orientation:
                raise ValueError('Not Valid Slide')
            else:
                self.valid = 1
        else:
            self.valid = 1