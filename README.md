- Реализовать генератор случайных 1 и 0 с помощью одномерного автомата по правилу 30.
  + Если центральная ячейка заполнена, то 1, если пустая - 0.
  + Напишите модуль `rule_30.py` и сохраните его в корневой директории в котором будет реализован генератор gen случайных 1 и 0.
  + В репозитории находится файл `test.py`, который импортирует `gen` из файла `rule_30.py`. При запуске теста командой `python -m unittest test.py` пользователь вводит число, чтобы пропустить несколько итераций, затем проверяются следующие сгенерированные значения. Так как генератор случайный и детерминированный, то проверка с очень большой долей вероятности пройдёт только если пользователь введёт определённое число.
- Как проходит проверка:
  + Вы присылаете мне (morozov6420@gmail.com) либо код модуля `rule_30.py`, либо ссылку на свой репозиторий. 
  + Я запускаю тест, ввожу загаданное заранее число, если тест сработает, значит всё работает верно. Если будут ошибки, я посмотрю код, постараюсь дать комментарий (с репозиторием это будет продуктивнее).
