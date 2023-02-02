import os
import time
import csv
import requests
from bs4 import BeautifulSoup

# 영화 리뷰 크롤링 함수
def get_movie_review(page_number):
  URL = "https://movie.naver.com/movie/point/af/list.naver?&page="
  samples = []
  for i in range(1, page_number + 1):
    response = requests.get(URL+str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    review_list = soup.find_all(name='td', attrs={'class': 'title'})
    for review in review_list:
      movie_title = review.find(name='a', attrs={'class': 'movie color_b'}).string
      movie_review_sentence = review.find(name='a', attrs={'class': 'report'}).get('onclick').split('\',')[2][2:]
      movie_score = review.find('em').string
      sample = [movie_title, movie_review_sentence, int(movie_score)]
      if movie_review_sentence:
        samples.append(sample)
    # 0.5초 (DDOS 분류 방지)
    time.sleep(0.5)
  return samples

# CSV 파일 쓰기 함수
def get_csv_file(samples):
  header = ['movie', 'sentence', 'score']
  cwd = os.getcwd()
  with open(cwd + '/samples.csv', 'w', encoding='utf-8', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(header)
    writer.writerows([item for item in sample] for sample in samples)
    fd.close()

sample_reviews = get_movie_review(150)
get_csv_file(sample_reviews)