# from spellchecker import spellchecker
# corrector = spellchecker()

# word = input("entre word : ")


# if word in corrector:
    
#     print("correct")

# else:
#     correct_word = corrector.correction(word)
#     print("correct spelling is : " , correct_word)


from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter word: ")

if corrector.correction(word) == word:
    print("Correct")
else:
    corrected_word = corrector.correction(word)
    print("Correct spelling is:", corrected_word)
