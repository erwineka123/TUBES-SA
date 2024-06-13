# Memasukkan kamus kata yang akan diuji coba
dictionary = {"NEW", "SEA", "WEST", "ALL"}

# Membuat set prefix dari kamus untuk cek cepat
prefix_set = set()
for word in dictionary:
    for i in range(1, len(word)):
        prefix_set.add(word[:i])
        
# Aturan permaianan Boggle, pola langkah
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

# Periksa kata dalam grid
def valid(x, y, visit, board):
    return (0 <= x < len(board)) and (0 <= y < len(board[0])) and not visit[x][y]

# Algoritma Backtracking
def backtrackingSearchWord(board, visit, i, j, current_word):
    visit[i][j] = True
    current_word += board[i][j]

    if current_word in dictionary:
        found_words.add(current_word)

    for x in range(8):
        nextI, nextJ = i + row[x], j + col[x]
        if valid(nextI, nextJ, visit, board):
            backtrackingSearchWord(board, visit, nextI, nextJ, current_word)

    visit[i][j] = False

# Algoritma Branch and Bound
def branch_and_bound(board, visited, i, j, current_word, found_words):
    if not (0 <= i < len(board) and 0 <= j < len(board[0])):
        return

    if visited[i][j]:
        return

    current_word += board[i][j]
    visited[i][j] = True

    if len(current_word) >= 3 and current_word in dictionary:
        found_words.add(current_word)

    # Melakukan pruning ketika current_word bukan awalan dari kata dalam kamus.
    if current_word not in prefix_set and current_word not in dictionary:
        visited[i][j] = False
        return

    for k in range(8):
        next_i, next_j = i + row[k], j + col[k]
        if valid(next_i, next_j, visited, board):
            branch_and_bound(board, visited, next_i, next_j, current_word, found_words)

    visited[i][j] = False

def find_words_backtrackingSearchWord(board):
    global found_words
    found_words = set()
    visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            backtrackingSearchWord(board, visit, i, j, "")

    return found_words

def find_words_branch_and_bound(board):
    found_words = set()
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            branch_and_bound(board, visited, i, j, "", found_words)

    return found_words
