import csv
import os

class RawMovieReview:

    def __init__(self, file_name: str = 'samples.csv'):
        self._file_name = file_name
        self._path = os.getcwd() + '/'
        self.__dataset = []

        with open(self._path + self._file_name, 'r', encoding='utf-8') as fd:
            reader = csv.reader(x.replace('\0', '') for x in fd)
            idx = 0
            for entry in reader:
                if idx != 0:
                    self.__dataset.append((entry[0], entry[1], int(entry[2])))
                idx += 1

    # indexing (0부터 시작하여 len(dataset) - 1 번째까지 indexing 가능)
    def __getitem__(self, index):
        if index > len(self.__dataset):
            raise IndexError()
        return self.__dataset[index]

    # dataset 내부의 리뷰 개수를 조회
    def __len__(self):
        return len(self.__dataset)

