import tkinter as tk
from tkinter import messagebox, Checkbutton, IntVar
import pandas as pd

class RestaurantRecommendationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("숙명여대 앞 맛집 추천 시스템")
        self.root.geometry("600x500")  # 창 사이즈를 4배로 키움
        
        self.responses = []
        self.data = pd.DataFrame(columns=['Question', 'Response'])
        
        self.create_question_1()

    def create_question_1(self):
        self.clear_window()
        
        question = "다음 중 가려는 장소의 유형을 고르시오."
        self.label = tk.Label(self.root, text=question, font=("Helvetica", 13))
        self.label.pack()
        
        self.place_type = tk.StringVar(value="")
        options = ["카페", "식당", "술집"]
        
        for option in options:
            rb = tk.Radiobutton(self.root, text=option, variable=self.place_type, value=option, font=("Helvetica", 13), indicatoron=1)
            rb.pack(anchor='w')
        
        confirm_button = tk.Button(self.root, text="확인", command=self.handle_question_1, font=("Helvetica", 13))
        confirm_button.pack()
        
    def handle_question_1(self):
        response = self.place_type.get()
        if response:
            self.responses.append(("가려는 장소의 유형", response))
            if response == "식당":
                self.create_restaurant_question()
            elif response == "카페":
                self.create_cafe_question()
            elif response == "술집":
                self.create_pub_question()
        else:
            messagebox.showwarning("경고", "장소의 유형을 선택해주세요.")
    
    def create_restaurant_question(self):
        self.clear_window()
        
        question1 = "선호하는 음식 종류를 모두 골라 주시오."
        self.label1 = tk.Label(self.root, text=question1, font=("Helvetica", 13))
        self.label1.pack()
        
        self.food_types = {
            "한식": IntVar(value=1), "양식": IntVar(value=1), "일식": IntVar(value=1),
            "중식": IntVar(value=1), "고기구이": IntVar(value=1), "버거": IntVar(value=1), "기타": IntVar(value=1)
        }
        
        for food, var in self.food_types.items():
            cb = Checkbutton(self.root, text=food, variable=var, font=("Helvetica", 13))
            cb.pack(anchor='w')
        
        question2 = "식당을 고를 때 가장 중요하게 볼 특성 3가지를 선택하시오."
        self.label2 = tk.Label(self.root, text=question2, font=("Helvetica", 13))
        self.label2.pack()
        
        self.restaurant_preferences = {
            "맛있는 음식": IntVar(), "신선한 재료": IntVar(), "친절한 서비스": IntVar(),
            "청결한 매장": IntVar(), "차분한 분위기": IntVar(), "특별한 날 가기 좋음": IntVar(),
            "대화하기 좋음": IntVar(), "혼밥할 수 있음": IntVar()
        }
        
        for pref, var in self.restaurant_preferences.items():
            cb = Checkbutton(self.root, text=pref, variable=var, font=("Helvetica", 13))
            cb.pack(anchor='w')
        
        confirm_button = tk.Button(self.root, text="다음", command=self.handle_restaurant_question, font=("Helvetica", 13))
        confirm_button.pack()
        
    def handle_restaurant_question(self):
        selected_food_types = [food for food, var in self.food_types.items() if var.get() == 1]
        selected_preferences = [pref for pref, var in self.restaurant_preferences.items() if var.get() == 1]
        
        if len(selected_preferences) == 3:
            self.responses.append(("선호하는 음식 종류", ', '.join(selected_food_types)))
            self.responses.append(("중요한 특성", ', '.join(selected_preferences)))
            self.create_final_question()
        else:
            messagebox.showwarning("알림", "특성을 3가지 선택해주세요.")
    
    def create_cafe_question(self):
        self.clear_window()
        
        question = "카페를 고를 때 가장 중요하게 볼 특성 3가지를 선택하시오."
        self.label = tk.Label(self.root, text=question, font=("Helvetica", 13))
        self.label.pack()
        
        self.cafe_preferences = {
            "맛있는 커피": IntVar(), "맛있는 디저트": IntVar(), "친절한 서비스": IntVar(),
            "청결한 매장": IntVar(), "차분한 분위기": IntVar(), "공부하기 좋음": IntVar(),
            "대화하기 좋음": IntVar(), "특별한 메뉴가 있음": IntVar()
        }
        
        for pref, var in self.cafe_preferences.items():
            cb = Checkbutton(self.root, text=pref, variable=var, font=("Helvetica", 13))
            cb.pack(anchor='w')
        
        confirm_button = tk.Button(self.root, text="다음", command=self.handle_cafe_question, font=("Helvetica", 13))
        confirm_button.pack()
        
    def handle_cafe_question(self):
        selected_preferences = [pref for pref, var in self.cafe_preferences.items() if var.get() == 1]
        
        if len(selected_preferences) == 3:
            self.responses.append(("카페 중요 특성", ', '.join(selected_preferences)))
            self.create_final_question()
        else:
            messagebox.showwarning("알림", "특성을 3가지 선택해주세요.")
    
    def create_pub_question(self):
        self.clear_window()
        
        question = "술집을 고를 때 가장 중요하게 볼 특성 3가지를 선택하시오."
        self.label = tk.Label(self.root, text=question, font=("Helvetica", 13))
        self.label.pack()
        
        self.pub_preferences = {
            "맛있는 안주": IntVar(), "술의 종류가 다양함": IntVar(), "친절한 서비스": IntVar(),
            "청결한 매장": IntVar(), "독특한 컨셉": IntVar(), "특별한 날 가기 좋음": IntVar(),
            "대화하기 좋음": IntVar(), "혼술할 수 있음": IntVar()
        }
        
        for pref, var in self.pub_preferences.items():
            cb = Checkbutton(self.root, text=pref, variable=var, font=("Helvetica", 13))
            cb.pack(anchor='w')
        
        confirm_button = tk.Button(self.root, text="다음", command=self.handle_pub_question, font=("Helvetica", 13))
        confirm_button.pack()
        
    def handle_pub_question(self):
        selected_preferences = [pref for pref, var in self.pub_preferences.items() if var.get() == 1]
        
        if len(selected_preferences) == 3:
            self.responses.append(("술집 중요 특성", ', '.join(selected_preferences)))
            self.create_final_question()
        else:
            messagebox.showwarning("알림", "특성을 3가지 선택해주세요.")
    
    def create_final_question(self):
        self.clear_window()
        
        question = "별도로 원하는 사항이 있으신가요?"
        self.label = tk.Label(self.root, text=question, font=("Helvetica", 13))
        self.label.pack()
        
        self.additional_input = tk.Entry(self.root, width=50, font=("Helvetica", 13))
        self.additional_input.pack()
        
        confirm_button = tk.Button(self.root, text="완료", command=self.handle_final_question, font=("Helvetica", 13))
        confirm_button.pack()
        
    def handle_final_question(self):
        additional_response = self.additional_input.get()
        self.responses.append(("별도로 원하는 사항", additional_response))
        
        for question, response in self.responses:
            self.data = pd.concat([self.data, pd.DataFrame([{'Question': question, 'Response': response}])], ignore_index=True)
        
        # Display the collected data
        print(self.data)
        messagebox.showinfo("완료", f"응답이 저장되었습니다. 콘솔에서 데이터를 확인하세요.\n\n{self.data}")
        self.root.quit()
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantRecommendationSystem(root)
    root.mainloop()
