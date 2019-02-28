
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
            self.tags = images[0].tags | images[1].tags
            if images[0].orientation != 'V' or images[1].orientation != 'V':
                raise ValueError('Not Valid Slide')
            else:
                self.valid = 1
        else:
            self.tags = images[0].tags
            self.valid = 1
            if images[0].orientation != 'H':
                raise ValueError('Not Valid Slide')
