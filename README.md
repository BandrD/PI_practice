# SE_DevAidAI

Падеров Анатолий Викторович РИМ-130907  

Катеренчук Ярослав Сергеевич РИМ-130906​

Бобрешов Виталий Сергеевич РИМ-130906  

Деревянкин Александр Александрович РИМ-130907


Описание проекта

Цель этого научного проекта состоит в том, чтобы использовать модель BERT для классификации текста, разделяя обычный текст от кода на языке программирования Python. Мы планируем дообучить предварительно обученную модель BERT на нашем небольшом датасете, чтобы она могла правильно классифицировать текст.

Задачи проекта

1. Подготовка данных: Создание датасета, состоящего из примеров текста. Разделение данных на обучающую и тестовую выборки.
2. Загрузка предварительно обученной модели BERT, которая предварительно обучена на большом объеме текстов.
3. Подготовка данных для модели BERT: Преобразование данных в формат, понятный для модели BERT, с использованием токенизатора и добавлением специальных токенов.
4. Обучение модели BERT: Дообучение модели на нашем датасете с использованием техники дообучения (fine-tuning). Настройка параметров обучения, таких как размер пакета, скорость обучения и количество эпох.
5. Оценка производительности модели: Оценка производительности модели на тестовой выборке с использованием метрик, таких как точность и полнота.

Заключение

В рамках этого научного проекта, мы планируем использовать предварительно обученную модель BERT для классификации позитивных и негативных комментариев, а также для предсказания поведения пользователя на основании суммарных эмоций. Мы будем дообучать модель на нашем датасете, чтобы она смогла точно определять эмоциональную окраску комментариев и предсказывать возможное поведение пользователя. Это исследование может быть полезным для автоматического анализа и обработки текста на Python, а также для создания инструмента, способного предсказывать поведение пользователей на основе их эмоциональной реакции.

<b>Для запуска приложения используйте команду:</b> <code>docker-compose up -d</code> 
