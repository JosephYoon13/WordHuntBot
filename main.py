from mouse.mouse_control import MouseControl
import trie

# directions_list = [[(0, 1), (1, 0), (2, 0), (3, 0), (2, 1), (1, 1), (1, 2)],
#               [(0, 2), (0, 1), (1, 0), (1, 1), (2, 1), (3, 0), (3, 1)]
#               ]

# directions_list = [[(1, 2), (2, 1)],
#               [(0, 2), (1, 1)]
#               ]

if __name__ == "__main__":
    # print("Input board: ")
    # text = input()

    # t = trie.Trie()
    # hugelist = []
    # with open("dictionary.txt", "r") as f:
    #     hugelist = f.read().split()

    # for word in hugelist:
    #     t.insert(word.lower())


    # found_words = {}
    # directions = []
    # visited = []
    # matrix = [[None for c in range(4)] for r in range(4)]

    # k = 0
    # for m in range(4):
    #     for n in range(4):
    #         matrix[m][n] = text[k]
    #         k += 1

    # def recurse(i, j, dir, word):
    #     if i < 0 or j < 0 or i > 3 or j > 3:
    #         return
    #     if not t.startsWith(word) or (i, j) in visited:
    #         return

    #     word += matrix[i][j]
    #     visited.append((i, j))
    #     directions.append(dir)

    #     if len(word) >= 3 and t.search(word) and word not in found_words:
    #         found_words[word] = list(directions)

    #     recurse(i, j + 1, (i, j + 1), word)
    #     recurse(i, j - 1, (i, j - 1), word)
    #     recurse(i + 1, j, (i + 1, j), word)
    #     recurse(i - 1, j, (i - 1, j), word)
    #     recurse(i + 1, j + 1, (i + 1, j + 1), word)
    #     recurse(i + 1, j - 1, (i + 1, j - 1), word)
    #     recurse(i - 1, j + 1, (i - 1, j + 1), word)
    #     recurse(i - 1, j - 1, (i - 1, j - 1), word)
    #     del visited[-1]
    #     del directions[-1]
    #     word = word[:-1]

    # for i in range(4):
    #     for j in range(4):
    #         recurse(i, j, (i, j), '')

    # found_words = dict(
    #     sorted(found_words.items(), key=lambda x: len(x[0]), reverse=True))

    # for w, d in found_words.items():
    #     print(w, d)
    # print(len(found_words))
   
    # directions_list = found_words.values()

    directions_list = []

    # Open the text file in read mode
    with open('out.txt', 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line by commas and convert elements back to integers
            data_elements = line.strip().split(', ')
            # Convert elements into tuple pairs and append to the list
            tuples_list = [(int(data_elements[i]), int(data_elements[i+1])) for i in range(0, len(data_elements), 2)]
            directions_list.append(tuples_list)


    mouse = MouseControl()
    mouse.prepare()
    # directions = directions_list[0]
    # d = directions[0]
    # x, y = d
    # mouse.goto(1,2)
    # mouse.goto(0, 3)
    
    for directions in directions_list:
        init_x, init_y = directions[0]
        mouse.goto(init_x, init_y)
        mouse.press()
        for d in directions:
            x, y = d
            mouse.move(x, y)
        mouse.press()
        for d in reversed(directions):
            x, y = d
            mouse.moveReverse(x, y)

