# py01_gpt_clone.py

from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 사용
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import *
from tkinter.font import *

# Gemini를 위한 모듈
import google.generativeai as genai

# 6. Gemini 
genai.configure(api_key='AIzaSyBHc0oNJFPryYiXVl9wOjVnfKm6js5ngns') # 신청한 API 키 
model = genai.GenerativeModel('gemini-1.5-flash') # AI 사전 훈련된 모델


# 4. 전송버튼 이벤트
def responseMessage():
    # showinfo('실행', '--API를 실행합니다--')
    inputText = textMessage.get('1.0', END).replace('\n', '').strip() # 여백 없애기
    # showinfo('결과',inputText) # 다이얼로그, 모달(Modal)창
    print(inputText)
    textMessage.delete('1.0', END) 
    
    
    if inputText : # 사용자가 질문한 내용이 남음
        try :
            textResult.insert(END, '유저:', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트
            
            
            ai_response = model.generate_content(inputText)
            response = ai_response.text

            textResult.insert(END, 'chatBot :', BOLD)
            textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 아규먼트
            
        except Exception as e:
            textResult.insert(END, f'{str(e)}\n\n', 'error')
        
        finally:
            textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운


#. 8. textMessage 위젯에서 엔터를 치면 전송버튼이 클릭
def keypress(event):
    # print(repr(event.char)) # repr 안쓰면 \r, \x80표시 안됨
    #\r(캐리지 리턴),\n(뉴라인) 혼용해서 사용 \r\n, \n,\r
    
    if event.char == '\r':
        responseMessage()
        
        
## 11. 종료시 이벤트 처리 함수
def onClosing():
    if askyesno('종료확인', '종료하시겠습니까?'):  # askyesno -> 팝업창에 예/아니요  
        root.destroy() # 완전히 종료

        

# 1. 메인윈도우 생성
root = Tk()

root.title('Gemini chatBot')
root.geometry('730x450')


# 12. 아이콘 변경
#./image/경로는 삭제
root.iconbitmap('kitty.ico') # pyinstaller 때는 실행파일폴더에 icon 복사


# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
myFont = Font(family='NanumGothic', size= 13)
boldFont = Font(family='NanumGothic', size=13, weight=BOLD, slant=ITALIC)


# 2.UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF') # inputFrame을 만들어야 text 만들기 가능 
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button을 구성 
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont) # 글자순으로 자동 줄바꿈 하겠다



# 8. 입력창에서 엔터를 치면 이벤트 발생 
textMessage.bind('<Key>', keypress) #keypress 이벤트 처리함수 발생
textMessage.pack(side=LEFT,padx=15)


buttonSend = Button(inputFrame, text='전송', bg='#EA4335', fg='white',
                    font=myFont, command=responseMessage)
buttonSend.pack(side=RIGHT, padx=20, pady=5)



# 5. 출력될 API 호출 결과 메세지 스크롤기능 텍스트위젯
textResult = ScrolledText(root, wrap=WORD, bg='#23A8F2', fg='white', font=myFont)
textResult.pack(fill=BOTH,expand=True)
# text - 여러줄 삽입 가능
# entry - 한 줄 삽입 가능
# wrap = 자동 줄바꿈
# fill = 채우다 

# 10. 스크롤텍스트에 출력될 메세지 디자인 
textResult.tag_configure('user', font=boldFont, foreground='#094ED9')
textResult.tag_configure('ai', font=boldFont, foreground='#233B62')
textResult.tag_configure('error', font=boldFont, foreground='red')



# 9. 실행 후, 입력창에 포커스가 자동으로 위치
textMessage.focus_set()


# 11. 프로그램 종료 버튼(x)을 누르면 종료메세지 출력되고 종료
root.protocol('WM_DELETE_WINDOW', onClosing) 


# 1.종료시까지 계속 실행
root.mainloop() 
