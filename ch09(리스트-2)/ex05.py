countries = ["Korea", "Spain", "Colombia", "USA", "Japan"]
countries_first_word = [word[0] for word in countries]
print("countries_first_word:", countries_first_word)

countries_final_word = [word[len(word)-1] for word in countries]
print("countries_final_word:", countries_final_word)

countries_words_len = [len(word) for word in countries]
print("countries_words_len:", countries_words_len)

colors = ["red", "green", "blue", "yellow", "magenta"]
cars = ["polstar2", "model Y", "santafe", "sorento", "bronco", "X5"]
cars_models = [x + "-" + y
                for x in colors
                for y in cars]
print("cars_models:", cars_models)