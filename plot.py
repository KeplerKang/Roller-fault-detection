import numpy as np


def get_table(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    table = np.zeros((len1 + 1, len2 + 1))
    table[:, 0] = range(len1 + 1)
    table[0, :] = range(len2 + 1)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            d1 = table[i - 1, j] + 1
            d2 = table[i - 1, j - 1] + 2 * (word1[i - 1] != word2[j - 1])
            d3 = table[i, j-1] + 1
            print(f"d[{i},{j}]=min:")
            print(f"d[{i - 1},{j}]+in[word1[{i}]]={d1}")
            print(f"d[{i - 1},{j - 1}]+sub[word1[{i}],word2[{j}]]={d2}")
            print(f"d[{i},{j - 1}]+del[word2[{j}]]={d3}")
            print()
            table[i, j] = min([d1, d2, d3])
    return table


if __name__ == '__main__':
    word1 = input('输入词1:')
    word2 = input('输入词2:')
    print(np.flip(get_table(word1, word2), axis=0))  # 上下颠倒
