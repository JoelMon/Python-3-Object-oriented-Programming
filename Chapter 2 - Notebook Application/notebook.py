import datetime

# Stores the last id used in a note.
last_id = 0


class Note:
    """
    A note within the notebook
    """

    def __init__(self, memo, tags=''):
        """Init with a memo and an optinal tag(s)"""

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """If text from filter is found in memo then return true"""
        return filter in self.memo or filter in self.tags


if __name__ == '__main__':
    print(f'{__name__} is not a script.')
