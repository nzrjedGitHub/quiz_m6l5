# Тут буде код веб-програми
from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after



def index():
   # max_quiz = 3
   # або якщо учень написав get_quiz_count(), то можна її імпортувати та вказати:
   # max_quiz = get_quiz_count[0] 
   # session['quiz'] = randint(1, max_quiz)
   # або якщо учень написав get_random_quiz_id(), то можна її імпортувати та вказати:
   # session['quiz'] = get_random_quiz_id()
   session['quiz'] = 1
   session['last_question'] = 0
   return '<a href="/test">Тест</a>'

def test():
   result = get_question_after(session['last_question'], session['quiz'])
   if result is None or len(result) == 0:
       return redirect(url_for('result'))
   else:
       session['last_question'] = result[0]
       return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'

def result():
   return "that's all folks!"

# Створюємо об'єкт веб-програми:
app = Flask(__name__) 
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/test', 'test', test) # створює правило для URL '/test'
app.add_url_rule('/result', 'result', result) # створює правило для URL '/test'
# Встановлюємо ключ шифрування:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   # Запускаємо веб-сервер:
   app.run()
