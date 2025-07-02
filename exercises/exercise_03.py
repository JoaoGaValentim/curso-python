# Exercício - sistema de perguntas e respostas

questions = [
    {"question": "Quanto é 2x2?", "options": [4, 8, 3, 10], "response": 4},
    {"question": "Quanto é 2x5?", "options": [4, 8, 3, 10], "response": 10},
    {"question": "Quanto é 3x1?", "options": [4, 8, 3, 10], "response": 3},
    {
        "question": "Quem é(são) o(s) melhor(es) avô(s) do mundo?",
        "options": ["Tobias/Sebastião", "Sagui", "Lula", "Moraes"],
        "response": "Tobias/Sebastião",
    },
]

count_total_questions = 0
score_correct = 0
score_errors = 0

while count_total_questions < len(questions):
    question_text = questions[count_total_questions]["question"]
    question_options = questions[count_total_questions]["options"]
    question_response = questions[count_total_questions]["response"]

    print(question_text)

    question_responses = []
    for index, option in enumerate(question_options, start=1):
        print(f"{index}) {option}")
        question_responses.append({f"{index}": option})

    user_option_input = input("Qual é a resposta ? ")

    if not user_option_input.isdigit():
        print("Informe uma alternativa válida! (Ex.: 1, 2, 3...)")
        continue

    for _, question in enumerate(question_responses):
        if question.get(user_option_input):
            is_correct = question.get(user_option_input) == question_response
            if is_correct:
                print("Parabéns! Você acertou! ✅")
                score_correct += 1
            if not is_correct:
                print("Opa! Você errou! ❌")
                score_errors += 1

    count_total_questions += 1


print("=" * 10)
print(f"ACERTOS => {score_correct}".center(10))
print(f"ERROS => {score_errors}".center(10))
print("=" * 10)
