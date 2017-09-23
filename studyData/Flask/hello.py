from flask import Flask


app = Flask(__name__) # 앱을 메인에서 실행하겠다는 의미임.(터미널에서 실행 하겠다는 의미..?)


# Flask 는 모두 함수형으로 정의되어 있음.

@app.route('/')

def index(): 
     return "hello flask"


if __name__ == "__name__":
     app.run(host= '127.0.0.1') # 아래부터 서버가 실제로 돌아가는 부분.
     
