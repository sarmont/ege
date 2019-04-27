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
            nums_search[search_list.index(word)]

#sort nums_search -> search_list
k = len(nums_search)
for i in range(k-1):
    for j in range(1, k):
        if nums_search[i] < nums_search[j]:
            nums_search[i], nums_search[j] = nums_search[j], nums_search[i]
            search_list[i], search_list[j] = search_list[j], search_list[i]
print(search_list, nums_search)
if k < 4:
    for a in search_list:
        print(a)
else:
    for i in range(k):
        if nums_search[i] <= nums_search[2]:
            print(search_list[i])
