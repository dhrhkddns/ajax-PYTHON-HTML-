from flask import Flask, jsonify, render_template
import random
import threading
from colorama import init, Fore
#작업 디렉토리가 달라서 설정해주고 실시간으로 변하는 변수를 다른 py파일에서 받아온다.
import sys
sys.path.append('C:/Users/omyra/OneDrive/바탕 화면/segment_detection_합치기_프로젝트')

import yolov8_region_counter

# colorama 초기화
init(autoreset=True)


app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)  # 'age' 키에 대한 값만 반환

@app.route('/', methods=['GET'])
def home():
    return render_template('golf.html')

@app.route('/gwangun', methods=['GET'])
def yoooo():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    print(Fore.BLUE +"python return 했음")
    return str(random.randint(1, 10))
    

@app.route('/golf_score', methods=['GET'])
def golf_score():
    
    return str(yolov8_region_counter.vid_frame_count)  # 'age' 키에 대한 값만 반환

if __name__ == '__main__':
    #스레드 생성
    t1 = threading.Thread(target=app.run)

    #스레드 시작
    t1.start()


print(Fore.BLUE + "wanna do BOTH AT THE SAME TIMEEEE!!")

#이 py를 영상인식 골프 py 결국에는 합쳐야한다....ㄷㄷ (홀에 들어간 스코어 변수를 html에 보여줘야함)