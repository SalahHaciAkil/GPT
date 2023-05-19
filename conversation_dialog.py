import openai
import os
import time
openai.api_key = open("openai_key.txt", "r").read().strip("\n")
questions = list()
bot_responses = list()
messages = list()

system_promote = "Answer as concisely as possible."
messages.append({"role": "system", "content": system_promote})

# add whilte loop
while True:
    # prompt the user to ask a question
    current_question = input("Me: ")
    if current_question.lower() in ['bye', 'goodbye', 'exit', 'quit']:
        print("Bot: Goodbye, have a nice day!")
        time.sleep(2)
        break

 
    if current_question == '':
        continue

    messages.append({"role": "user", "content": current_question})
    questions.append(current_question)


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        # max_tokens=3000,
    )

    current_response = response['choices'][0]['message']['content']
    print(f'\nChat Bot: {current_response}')
    bot_responses.append(current_response)
    messages.append({"role": "assistant", "content": current_response})

    print('\n' + '-' * 50 + '\n')


print("Chat history:")
for i in range(len(questions)):
    print(f"Q: {questions[i]}")
    print(f"A: {bot_responses[i]}")
    print('-' * 50)
    print()

