from flask import Flask
import random

app= Flask(__name__)
@app.route("/")

def 가즈아():
    def random_coin():
        outcome= random.choice(["앞", "뒤"])
        print("동전던지기 게임에 오신 것을 환영합니다! 당신의 운을 시험해 보세요")
        trial= input("\'앞\'이나 \'뒤\'를 입력하새요>")
        if outcome==trial:
            print("시작이 좋은걸요~ ")
            trial= input("\'앞\'이나 \'뒤\'를 입력하새요>")
            if outcome==trial:
                print("0.25의 확률을 뚫으셨군요! 당신은 럭키가이~")
                trial= input("\'앞\'이나 \'뒤\'를 입력하새요>")
                if outcome==trial:
                    print("대박, 당신은 열명중에 한명입니다!")
                else: 
                    print("당신의 운은 여기까진가요? 따라라~따라라라딴딴")    
            
            else: 
                print("당신의 운은 여기까진가요? 따라라~따라라라딴딴")
        else: 
            print("오늘 일진이 안좋군요 ㅎㅎ")
    return random_coin()
