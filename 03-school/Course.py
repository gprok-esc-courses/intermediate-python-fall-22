
class Course:
    def __init__(self, cid, title):
        self.id = cid
        self.title = title

    def __str__(self):
        return self.id + ". " + self.title


