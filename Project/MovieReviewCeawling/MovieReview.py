from RawMovieReview import RawMovieReview

class MovieReview(RawMovieReview):
    def __init__(self, file_name:str, score_threadhod:int):
        super().__init__(file_name)
        self._score_threadhold = score_threadhod

    def __getitem__(self, index):
        if index > super().__len__():
            raise IndexError()
        if super().__getitem__(index)[2] >= self._score_threadhold:
            return (super().__getitem__(index)[1].strip(), True)
        else:
            return (super().__getitem__(index)[1].strip(), False)