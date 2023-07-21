from collections import OrderedDict
import trie
# from image_processing import processImage


def main():

    # text = processImage()
    print("Input board: ")
    text = input()

    t = trie.Trie()
    hugelist = []
    with open("dictionary.txt", "r") as f:
        hugelist = f.read().split()

    for word in hugelist:
        t.insert(word.lower())

    # list = []
    # word = ''
    # def loop(node: trie.TrieNode, word: str):
    #     if node.children:
    #         for k, v in node.children.items():
    #             loop(v, word + k)
    #     else:
    #         list.append(word)

    # loop(cur, '')
    # print(list)

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

    for w, d in found_words.items():
        print(w, d)
    print(len(found_words))
    # if type(found_words['hia'][0]) is tuple:
    #     print('yes')


if __name__ == "__main__":
    main()
