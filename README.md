# Deep-Learning

## practice
## 1. Implement Back Propagation
  
    BackPropagation.ipynb
    
    reference : https://evan-moon.github.io/2018/07/19/deep-learning-backpropagation/

## 2. Implement LSTM model
    
    LSTM class
      - forward propagation
      - backward propagation

## Project
## 1. Lotto Predict
  
    LottoPred.ipynb

## 2. MovieReviewCrawling
<span style="background-color=green; color=green">2022-12-26</span>
### `RawMovieReview` 클래스는 다음을 준수해야 합니다.
1. 생성자
    * 생성자의 추가 인자는 `str`타입의 `file_name` 하나만을 받습니다.
    * `file_name` 인자의 기본값은 `"samples.csv"`입니다.
    * 해당 객체는 MovieReview.py에 의해 수집된 영화 리뷰에 대한 csv 파일을 다루는 객체입니다.
    * 모든 속성 값은 `protected` 홋은 `private`로 보호받습니다.
2. Indexing
    * 대괄호로 N번째 sample에 접근할 수 있습니다.
    * N은 0부터 시작합니다. `dataset[0]`은 첫번째 한줄 평 입니다.
    * Indexing 결과값은 `영화 이름, 한줄평, 점수`로 타입은 `(str, str, int)` 형태의 튜플입니다.
    * 대괄호로 읽기만 가능하고 수정은 불가능합니다.
3. Length
    * `len(dataset)`의 형태로 데이터셋 내의 한줄평 개수를 조회할 수 있습니다.

### `MovieReview` 클래스는 다음을 준수해야 합니다.
1. 상속
    * 위에서 정의한 `RawMoviewReview` 클래스를 상속받습니다.
    * `RawMoviewReview` 내의 데이터를 복사할 수 없습니다.
    * 저장된 `CSV`파일은 부모 클래스의 속성 혹은 메소드로 접근합니다.
2. 생성자
    * 생성자의 인자는 부모의 인자와 `int`타입의 `score_threadhold`를 받습니다.
    * 해당 자식 클래스에는 `CSV`파일 및 그 내용이 속성으로 들어갈 수 없습니다.
    * 영화 데이터는 부모에만 저장됩니다.
3. Indexing
    * Indexing 결과 값은 한줄평, 긍부정으로 타입은 `(str, bool)` 형태의 튜플입니다.
    * 점수가 객체의 `score_threadhold` 이상일 경우 긍정이 `True`, 미만이면 `False` 입니다.


## Data Analysis
## 1. OTTO kaggle Competition
