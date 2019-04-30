#Решение задачи из банка задачи ФИПИ
# Текст задачи по ссылке
# https://yadi.sk/i/wlURv0ycqDPVbA

abr = input()
n = int(input())

search_list = []
nums_search = []

for i in range(n):
    word_abr = ""
    word = input()

    word_abr = word_abr + word[0]

    for i in range(1, len(word)):
        if word[i] == " ":
            word_abr += word[i + 1]

    if word_abr == abr:
        if word not in search_list:
            search_list.append(word)
            nums_search.append(1)
        else:
            nums_search[search_list.index(word)] += 1

# sort nums_search -> search_list
k = len(nums_search)
for i in range(k - 1):
    for j in range(k - i - 1):
        if nums_search[j] < nums_search[j + 1]:
            nums_search[j], nums_search[j + 1] = nums_search[j + 1], nums_search[j]
            search_list[j], search_list[j + 1] = search_list[j + 1], search_list[j]


if k < 4:
    for a in search_list:
        print(a)
else:
    for i in range(k):
        if nums_search[i] >= nums_search[2]:
            print(search_list[i])
