from spellchecker import spellchecker
corrector = spellchecker

word = input("entre word : ")

if word in corrector:
    print("correct")

else:
    correct_word = corrector.correction(word)
    print("correct spelling is : " , correct_word)

