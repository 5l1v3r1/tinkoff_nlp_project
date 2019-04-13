# Проект: Болталка retrieval-based

## План разработки проекта

1. Препроцессинг данных (Cахаров).
Формирование из данных context-response пар, векторизация.
2. Создание архитектуры проекта (Сахаров, Воробьева) Retrieval-based, различные метрики.
4. Реализация телеграм-бота (Воробьева)

## Train 
'''
python3 main.py train <file_name> <num_epochs> <sentence_length> <vocab_size> <embed_dim>
'''

## Start telegram bot
'''
python3 main.py start_bot <token>
'''
