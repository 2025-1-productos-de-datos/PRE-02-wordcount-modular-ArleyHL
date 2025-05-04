# obtain a list
import os

from ._internals.write_count_words import write_count_words


def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


def main():

    input_file_list = os.listdir("data/input/")
    # all_lines = read_all_lines()

    counter = {}
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    write_count_words(counter)


if __name__ == "__main__":
    main()
