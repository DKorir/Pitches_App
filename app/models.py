from app.main import comment


class Pitch:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Comment:

    all_comments = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):

        response = []

        for review in cls.all_comments:
            if comment.movie_id == id:
                response.append(comment)

        return response