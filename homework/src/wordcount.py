# obtain a list
import os

from ._internals.write_count_words import write_count_words


def main():

    ##read all lines
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        file_path = os.path.join("data/input", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ##preprocess lines
    all_lines = [line.lower().strip() for line in all_lines]

    ##split in words
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())

    ##count words
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    #     counter = {}
    #     for filename in input_file_list:
    #         with open("data/input/" + filename) as f:
    #             for l in f:
    #                 for w in l.split():
    #                     w = w.lower().strip(",.!?")
    #                     counter[w] = counter.get(w, 0) + 1
    # //##
    write_count_words(counter)


if __name__ == "__main__":
    main()
