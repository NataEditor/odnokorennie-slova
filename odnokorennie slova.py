dictionary = ['разговор', 'говорить', 'ГОВОР', 'беседовать', 'наМ', 'Вместе']
word = 'говор'

same_word = []
def single_root_word(root_word, *other_word):

    same_word = []
    for item in other_word:
        if str(item).lower() in root_word.lower() or root_word.lower() in str(item).lower():
            #print(str(item))
            
            same_word.append(str(item).lower())
    print(same_word)    

single_root_word(word, dictionary)



print('поветка работы цикла и условия не в функции')


for item in dictionary:
    if str(item).lower() in word.lower() or word.lower() in str(item).lower():
        #print(str(item))
        same_word.append(str(item).lower())
print(same_word)    