#obtain a list
import os

def main():
     
    input_file_list=os.listdir('data/input/')

    counter={}
    for filename in input_file_list:
        with open('data/input/'+filename) as f:
            for l in f:
                for w in l.split( ):
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    write_count_words(counter)

def write_count_words(counter):
    if not os.path.exists('data/output'):
        os.makedirs('data/output')

    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
            for key, value in counter.items():
                f.write(f"{key}\t{value}\n")

if __name__ == "__main__":
     main()