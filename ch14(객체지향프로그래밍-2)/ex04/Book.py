class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s \nAuthor: %s" % (self.title, self.author)

    def len(self):
        return self.pages