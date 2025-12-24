# %%
import pandas as pd
import numpy as np

# %%
cafe_data = pd.read_csv("C:/dacos_rec/crawling/df_cafe(2).csv", encoding='euc-kr')
pub_data = pd.read_csv("C:/dacos_rec/crawling/df_drink(2).csv", encoding='euc-kr')
restaurant_data = pd.read_csv("C:/dacos_rec/crawling/df_meal (3).csv", encoding='euc-kr')
    

# %%
# 모든 데이터를 통합
all_data = pd.concat([cafe_data, restaurant_data, pub_data], ignore_index=True)

# %%
# 사용자 선택지 정의
category_options = {
    '식당': ['한식', '중식', '일식', '양식', '육류', '아시안음식', '샐러드'],
    '주점': ['이자카야', '맥주', '와인', '바', '요리주점'],
    '카페': ['카페', '디저트 카페', '베이커리', '브런치 카페', '특별 메뉴']
}

# %%
# 선택지 정의
options = {
    '식당': {
        'categories': ['한식', '중식', '양식', '육류'],
        'tags': {
            '맛': ['음식이 맛있어요', '빵이 맛있어요'],
            '특별한 메뉴': ['특별한 메뉴가 있어요'],
            '메뉴 다양성': ['메뉴 구성이 알차요'],
            '신선도': ['재료가 신선해요', '잡내가 적어요', '고기 질이 좋아요'],
            '가성비': ['가성비가 좋아요', '양이 많아요'],
            '서비스': ['친절해요', '반찬이 잘 나와요', '음식이 빨리 나와요'],
            '청결': ['매장이 청결해요', '화장실이 깨끗해요'],
        }
    },
    '카페': {
        'categories': ['베이커리', '디저트'],
        'tags': {
            '맛': ['커피가 맛있어요', '디저트가 맛있어요'],
            '청결': ['매장이 청결해요', '화장실이 깨끗해요'],
            '서비스': ['친절해요', '포장이 깔끔해요'],
            '분위기': ['아늑해요', '인테리어가 멋져요'],
        }
    },
    '술집': {
        'categories': ['이자카야', '맥주', '바'],
        'tags': {
            '맛': ['음식이 맛있어요'],
            '서비스': ['친절해요'],
            '술 다양성': ['술이 다양해요'],
            '분위기': ['음악이 좋아요', '대화하기 좋아요'],
        }
    }
}

# %%
# 사용자 선택 시뮬레이션
def get_user_selection(prompt, choices):
    print(prompt)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    selection = int(input("선택하세요: ")) - 1
    return choices[selection]


# %%
# 1단계: 카테고리 선택
selected_category = get_user_selection("카테고리를 선택하세요:", list(category_options.keys()))

# %%
# 2단계: 세부 항목 선택
selected_subcategory = get_user_selection(f"{selected_category}의 세부 항목을 선택하세요:", category_options[selected_category])

# %%
# 3단계: 중요 태그 선택
selected_option = get_user_selection(f"{selected_category}에서 중요하게 생각하는 것을 선택하세요:", list(options[selected_category]['tags'].keys()))

# %%
# 카테고리 및 세부 항목 필터링
filtered_data = data[(data['FoodCategory'] == selected_category) & (data['FoodType'] == selected_subcategory)]

# %%
# 데이터 매핑
data_map = {'식당': meal_df, '카페': cafe_df, '술집': drink_df}
selected_data = data_map[selected_category]
selected_tags = options[selected_category]['tags'][selected_option]


# %%
# 음식 종류 필터링
filtered_data = selected_data[selected_data['FoodType'] == selected_food_type]


# %%
# 리뷰 기반 랭킹 생성
def rank_stores(data, tags, weight_absolute=0.8, weight_relative=0.2):
    # 절대적 리뷰 수 계산
    data['AbsoluteCount'] = data['Reviews'].apply(lambda x: sum(1 for tag in tags if tag in x))
    
    # 상대적 리뷰 수 계산
    data['RelativeCount'] = data['AbsoluteCount'] / data['Reviews'].str.split().apply(len)
    
    # 가중치 계산
    data['Score'] = (data['AbsoluteCount'] * weight_absolute) + (data['RelativeCount'] * weight_relative)
    
    # 랭킹 생성
    ranked_data = data.sort_values(by='Score', ascending=False)
    return ranked_data

# %%
# 랭킹 계산
ranked_results = rank_stores(filtered_data, selected_tags)

# %%
# 결과 출력
print(f"카테고리: {selected_category}, 음식 종류: {selected_food_type}, 선택지: {selected_option}")
print("추천 결과:")
print(ranked_results[['StoreName', 'Score', 'AbsoluteCount', 'RelativeCount']])


