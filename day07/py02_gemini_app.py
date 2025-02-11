# py02_gemini_app.py
from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *

# Gemini를 위한 모듈
import google.generativeai as genai

# 6. Gemini 
genai.configure(api_key='AIzaSyBHc0oNJFPryYiXVl9wOjVnfKm6js5ngns') # 신청한 API 키 
model = genai.GenerativeModel('gemini-1.5-flash') # AI 사전 훈련된



class window(Tk): # 부모의 클래스를 가지되, 재정의 => 오버라이딩
    
    def __init__(self): 
        super().__init__() # 부모객체도 같이 초기화 
        self.title('Gemini_ChatBot v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/kitty.ico') 
        # 클래스 작업할때 self...유심히
        self.protocol('WM_DELETE_WINDOW', self.onClosing)
        
        
        self.initWindow() # 윈도우 화면 초기화 멤버함수(메서드)
        
    def initWindow(self):
        # 폰트
        self.myFont = Font(family='NanumGothic', size= 13)
        self.boldFont = Font(family='NanumGothic', size=13, weight=BOLD, slant=ITALIC)    
        
        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF') # inputFrame을 만들어야 text 만들기 가능 
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)
        
        # 입력창
        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont)
        # 입력창에서 엔터를 치면 이벤트 발생
        self.textMessage.bind('<Key>', self.keypress)
        self.textMessage.pack(side=LEFT,padx=15)
        # 9. 실행 후, 입력창에 포커스가 자동으로 위치
        self.textMessage.focus_set()
        
        
        # 버튼
        self.buttonSend = Button(self.inputFrame, text='전송', bg='#EA4335', fg='white',
                    font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady=5)
        
    
        # 출력될 API 호출 결과 메세지 스크롤기능 텍스트위젯
        self.textResult = ScrolledText(self, wrap=WORD, bg='#23A8F2', fg='white', font=self.myFont)
        self.textResult.pack(fill=BOTH,expand=True)
        
        self.textResult.tag_configure('user', font=self.boldFont, foreground='#094ED9')
        self.textResult.tag_configure('ai', font=self.boldFont, foreground='#233B62')
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')
    
    
        
    #전송버튼
    def responseMessage(self): # 내용 수정
        # showinfo(f'동작', 
        #         f'이제 API를 호출하면 됩니다!\n{self.textMessage.get("1.0", END)}')
        self.inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()
        print(self.inputText)
        self.textMessage.delete('1.0', END)
        
        if self.inputText : # 사용자가 질문한 내용이 남음
            try :
                self.textResult.insert(END, '유저:', BOLD)
                self.textResult.insert(END, f'{self.inputText}\n\n', 'user') # 'user' 텍스트 아규먼트
                
                ai_response = model.generate_content(self.inputText)
                response = ai_response.text

                self.textResult.insert(END, 'chatBot :', BOLD)
                self.textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 아규먼트
            
            except Exception as e:
                self.textResult.insert(END, f'{str(e)}\n\n', 'error')
        
            finally:
                self.textResult.see(END)
        
    def keypress(self, event):
        if event.char == '\r':
            self.responseMessage()
            
    
        
        
    # 종료이벤트    
    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?') :
            self.destroy() # 완전종료
    
    
if __name__ == '__main__':
    print('-----Tkinker 클래스 시작!-----')
    app = window() # Tkinter 클래스 객체 생성
    app.mainloop()   
