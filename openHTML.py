from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_pic():
    with open('Route.txt', 'r') as f:
        list = f.readlines()
    final_path = []
    for i in list:
        final_path.append(i[0:len(i) - 1])
    return render_template('Show_Route.html',final_path = final_path)

if __name__ == '__main__':
    app.run(debug=True)