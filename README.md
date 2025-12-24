# 숙명여자대학교 맛집 추천 시스템

숙명여대 주변 맛집을 개인화된 방식으로 추천하는 시스템입니다. 태그 기반 필터링과 협업 필터링을 결합하여 사용자에게 맞는 맛집을 추천합니다.

## 📋 프로젝트 개요

이 프로젝트는 숙명여대 주변 맛집 데이터를 수집하고, 사용자의 선호도를 기반으로 개인화된 추천을 제공하는 시스템입니다.

### 주요 특징
- **개인화 추천**: 가게의 태그 비율과 사용자의 태그 비율을 비교하여 가장 유사한 맛집 추천
- **광고 기반이 아닌 추천**: 숨은 맛집도 추천 가능
- **다양한 필터링**: 클러스터링 기반 1차 필터링 후 태그 비율 비교
- **리뷰 데이터 활용**: BERT를 활용한 리뷰 분석 및 키워드 추출

## 👥 구성원

- 권도은,김다은,이서영,위지우


## 📁 프로젝트 구조

```
dacos_rec-main/
├── notebooks/          # Jupyter 노트북 파일들 (데이터 분석 및 모델링)
│   ├── clustering_1차.ipynb
│   ├── collaborative_recommendation.ipynb
│   ├── FINAL_collaborative_recommendation.ipynb
│   ├── keywordreview_prep.ipynb
│   ├── pca+cosine.ipynb
│   ├── restaurant+review.ipynb
│   ├── review_BERT.ipynb
│   ├── tagging_recommendation.ipynb
│   ├── user_input_based_filtering.ipynb
│   ├── user_review_vectorization.ipynb
│   └── ...
├── scripts/            # Python 스크립트 파일들
│   ├── recsys_UI.py                    # 추천 시스템 UI (Tkinter)
│   ├── recsys_UI_수정버전.py           # 수정된 UI 버전
│   ├── naver_KeywordReview.py          # 네이버 리뷰 크롤링
│   └── 필터링1차.py                    # 필터링 스크립트
├── data/               # 데이터 파일들
│   ├── aggregated_final_result.csv
│   ├── combined_restaurant_data.csv
│   ├── dacos_tagging_adjusted_sorted.csv
│   ├── df_cafe.csv
│   ├── df_drink.csv
│   ├── df_meal.csv
│   ├── result_cafe.csv
│   ├── result_drink.csv
│   ├── result_meal.csv
│   └── ...
├── archives/           # 압축 파일들
│   ├── naver_review_2024-11-11_15명.zip
│   ├── result_meal.zip
│   └── userreviews_50_csv (2).zip
└── README.md
```

## 🔧 주요 기능

### 1. 데이터 수집 및 전처리
- 네이버 플레이스 크롤링을 통한 맛집 정보 수집
- 리뷰 데이터 수집 및 전처리
- 태그 기반 데이터 정제

### 2. 추천 알고리즘
- **클러스터링**: 1차 필터링을 위한 클러스터링
- **태그 기반 추천**: 가게와 사용자의 태그 비율 비교
- **협업 필터링**: 사용자 기반 협업 필터링
- **PCA + 코사인 유사도**: 차원 축소 후 유사도 계산

### 3. 리뷰 분석
- BERT를 활용한 리뷰 벡터화
- 키워드 기반 리뷰 분석
- 사용자 리뷰 벡터화

### 4. 사용자 인터페이스
- Tkinter 기반 GUI
- 사용자 선호도 입력 받기
- 카페/식당/술집별 맞춤 질문

## 🚀 사용 방법

### 환경 설정

필요한 패키지 설치:
```bash
pip install pandas numpy scikit-learn tkinter transformers torch
```

### UI 실행

추천 시스템 UI 실행:
```bash
python scripts/recsys_UI.py
```

또는 수정 버전 실행:
```bash
python scripts/recsys_UI_수정버전.py
```

### 노트북 실행

Jupyter 노트북을 사용하여 데이터 분석 및 모델링:
```bash
jupyter notebook notebooks/
```

## 📊 데이터 설명

### 주요 데이터 파일
- `combined_restaurant_data.csv`: 통합된 맛집 데이터
- `dacos_tagging_adjusted_sorted.csv`: 태그가 조정된 정렬된 데이터
- `df_cafe.csv`, `df_drink.csv`, `df_meal.csv`: 카테고리별 데이터
- `result_*.csv`: 추천 결과 데이터

## 🔍 주요 노트북 설명

- `clustering_1차.ipynb`: 클러스터링을 통한 1차 필터링
- `collaborative_recommendation.ipynb`: 협업 필터링 구현
- `tagging_recommendation.ipynb`: 태그 기반 추천
- `review_BERT.ipynb`: BERT를 활용한 리뷰 분석
- `user_input_based_filtering.ipynb`: 사용자 입력 기반 필터링
- `pca+cosine.ipynb`: PCA와 코사인 유사도를 활용한 추천

## 🎯 향후 개선 방안

1. **개인화 강화**: 현재 태그 기반 추천의 한계를 극복하기 위한 개선
2. **정답 데이터 부재 문제**: 클러스터링으로 1차 필터링 후 비율 비교 방식 고도화
3. **리뷰 데이터 확장**: 추가 크롤링을 통한 데이터 확장
4. **모델 성능 향상**: 다양한 추천 알고리즘 조합 및 하이퍼파라미터 튜닝


## 📄 라이선스

이 프로젝트는 숙명여자대학교 데이터과학 프로젝트입니다.
