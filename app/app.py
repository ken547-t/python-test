import io
from flask import Flask, Response, render_template, request, send_file

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return '''
    Hello Flask!
    <br>
    <a href="/site_map">/site_map</a>
    '''

# 動作確認用のサイトマップ
@app.route('/site_map')
def site_map():
    # すべてのルート情報を取得
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(rule)
    return render_template("site_map.html", routes=routes)

# formの値を使用
@app.route('/get_form', methods=['GET', 'POST'])
def get_form():
    var_name = request.form.get('in_name')
    return render_template("index.html", out_name=var_name)

# パスパラメータを使用
@app.route("/hello/<name>")
def test(name):
    return f"<h1>Hello {name}!</h1>"

# ファイル出力
@app.route("/out_file")
def out_file():
    # メモリ内にファイルを生成
    file_content = "test"
    file = io.BytesIO(file_content.encode('utf-8'))
    file.seek(0)  # ファイルの先頭に戻る

    # ファイルをクライアントに送信
    return Response(
        file,
        mimetype='text/plain',
        headers={
            'Content-Disposition': 'attachment; filename=test.txt'
        }
    )
