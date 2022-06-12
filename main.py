import python


def main():
    name = input("Введите ваше имя:")

    words = python.get_words("words.txt")
    points_counter = 0

    for word in words:
        shuffled_word = python.shuffle_char_in_word(word)

        print(f"Угадайте слово:{shuffled_word}")
        user_answer = input("Ваш ответ: ")
        user_answer = user_answer.lower()

        if user_answer == word:
            print("Верно! Вы получаете 10 очков!")
            points_counter += 10

        else:
            print(f"Неверно! Верный ответ - {word}")

    python.save_user_result_to_History(name, points_counter)

    python.prin_statics()


if = __name__ = "__main__":
    main()