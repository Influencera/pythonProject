import json

from question import Question


def load_questions(filname='data/questions.json'):


    with open(filename, 'r', encoding='utf-8') as f_in:
        raw_questions = json.load(f_in)

        questions = []

        for raw_question in raw_questions:
            another_question = Question(
                raw_question.get("q"),
                int(raw_question.get("d")),
                raw_question.get("a")
            )

            questions.append(another_question)

        return questions


    def build_statistics(questions):


        correct_answers, total_answers, score = 0, 0 , 0

        for question in questions:
            total_answers += 1
            if question.is_correct():
                correct_answers += 1
                score += question.score

        return f"Отвечено {correct_answers} вопроса из {total_answers}\nНарано баллов: {score}"
