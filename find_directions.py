from collections import OrderedDict
import trie
from image_processing import processImage


def main():

    text = processImage()
    # print("Input board: ")
    # text = input()

    t = trie.Trie()
    hugelist = []
    with open("dictionary.txt", "r") as f:
        hugelist = f.read().split()

    for word in hugelist:
        t.insert(word.lower())

    found_words = {}
    directions = []
    visited = []
    matrix = [[None for c in range(4)] for r in range(4)]

    k = 0
    for m in range(4):
        for n in range(4):
            matrix[m][n] = text[k]
            k += 1

    def recurse(i, j, dir, word):
        if i < 0 or j < 0 or i > 3 or j > 3:
            return
        if not t.startsWith(word) or (i, j) in visited:
            return

        word += matrix[i][j]
        visited.append((i, j))
        directions.append(dir)

        if len(word) >= 3 and t.search(word) and word not in found_words:
            found_words[word] = list(directions)

        recurse(i, j + 1, (i, j + 1), word)
        recurse(i, j - 1, (i, j - 1), word)
        recurse(i + 1, j, (i + 1, j), word)
        recurse(i - 1, j, (i - 1, j), word)
        recurse(i + 1, j + 1, (i + 1, j + 1), word)
        recurse(i + 1, j - 1, (i + 1, j - 1), word)
        recurse(i - 1, j + 1, (i - 1, j + 1), word)
        recurse(i - 1, j - 1, (i - 1, j - 1), word)
        del visited[-1]
        del directions[-1]
        word = word[:-1]

    for i in range(4):
        for j in range(4):
            recurse(i, j, (i, j), '')

    found_words = dict(
        sorted(found_words.items(), key=lambda x: len(x[0]), reverse=True))

    directions = found_words.values()

   # Name of the output text file
    file_name = "out.txt"

    # Open the text file in write mode
    with open(file_name, 'w') as file:
        # Iterate through each list of tuples
        for sublist in directions:
            # Join each tuple elements as strings and join them with commas
            line = ', '.join(f"{elem[0]}, {elem[1]}" for elem in sublist)
            file.write(line + '\n')
            



    for w, d in found_words.items():
        print(w, d)
    print(len(found_words))
    # if type(found_words['hia'][0]) is tuple:
    #     print('yes')

    # loaded_data = []

    # # Open the text file in read mode
    # with open(file_name, 'r') as file:
    #     # Read each line from the file
    #     for line in file:
    #         # Split the line by commas and convert elements back to integers
    #         data_elements = line.strip().split(', ')
    #         # Convert elements into tuple pairs and append to the list
    #         tuples_list = [(int(data_elements[i]), int(data_elements[i+1])) for i in range(0, len(data_elements), 2)]
    #         loaded_data.append(tuples_list)

    # print(loaded_data)


if __name__ == "__main__":
    main()
