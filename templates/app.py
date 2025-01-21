from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # 获取当前文件所在目录的绝对路径
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # 设置模板文件夹的路径
    template_folder = os.path.join(dir_path, 'templates')
    app.template_folder = template_folder
    app.run(debug=True)