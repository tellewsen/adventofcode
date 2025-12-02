import numpy as np


def read_file(filename):
    with open(filename, "r") as f:
        file_input = [i.rstrip().lstrip().replace("  ", " ") for i in f.readlines()]
    return file_input


def fill_boards(file_content):
    boards = []
    marks = []
    for i in range(2, len(file_content), 6):
        grid = np.zeros((5, 5), dtype=int)
        for i, line in enumerate(file_content[i : i + 5]):
            numbers = line.split(" ")
            for j in range(len(numbers)):
                grid[i][j] = int(numbers[j])
        boards.append(grid)
        marks.append(np.zeros((5, 5), dtype=int))
    return boards, marks


def has_won(board):
    for i in range(5):
        if np.all(board[i, :] == 1):
            return True
        if np.all(board[:, i] == 1):
            return True
    return False


def get_score(board, marks):
    count = 0
    for i in range(5):
        for j in range(5):
            if marks[i][j] == 0:
                count += board[i][j]
    return count


def p1(boards, marks, numbers):
    for num in numbers:
        for i, board in enumerate(boards):
            location = np.where(board == num)
            if location:
                marks[i][location] = 1
            if has_won(marks[i]):
                win_marks = marks[i]
                return get_score(board, win_marks) * num
    raise Exception


def p2(boards, marks, numbers):
    has_won = set()
    board_len = len(boards)
    for num in numbers:
        for i, board in enumerate(boards):
            if i in has_won:
                continue
            location = np.where(board == num)
            if location:
                marks[i][location] = 1
            if has_won(marks[i]):
                has_won.add(i)
                if len(has_won) == board_len:
                    return get_score(board, marks[i]) * num
    raise Exception


def main():
    file_content = read_file("input.txt")
    bingo_numbers = [int(i) for i in file_content[0].split(",")]
    boards, marks = fill_boards(file_content)
    print(1, p1(boards.copy(), marks.copy(), bingo_numbers.copy()))
    print(2, p2(boards.copy(), marks.copy(), bingo_numbers.copy()))


if __name__ == "__main__":
    main()
