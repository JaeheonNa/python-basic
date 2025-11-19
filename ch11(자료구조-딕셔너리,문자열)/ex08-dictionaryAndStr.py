def countIngredient(string):
    ingredients = {'alpha': 0, 'digit': 0, 'space': 0}
    for i in string:
        if i.isalpha():
            ingredients['alpha'] = ingredients.get('alpha', 0) + 1
        if i.isdigit():
            ingredients['digit'] = ingredients.get('digit', 0) + 1
        if i.isspace():
            ingredients['space'] = ingredients.get('space', 0) + 1
    return ingredients

if __name__ == "__main__":
    string = input("문자열을 입력하시오: ")
    stringIngredient = countIngredient(string)
    print(stringIngredient)