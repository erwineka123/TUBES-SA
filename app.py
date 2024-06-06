from flask import Flask, render_template, jsonify, request
import boggleGame as boggle_bt
import boggleGame as boggle_bb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_words_bt', methods=['POST'])
@app.route('/find_words_bb', methods=['POST'])
def find_words():
    board = request.json.get('board')
    method = request.json.get('method', 'backtracking')
    if method == 'branch_and_bound':
        words = boggle_bb.find_words_branch_and_bound(board)
    else:
        words = boggle_bt.find_words_backtrackingSearchWord(board)
    return jsonify(list(words))

if __name__ == '__main__':
    app.run(debug=True)