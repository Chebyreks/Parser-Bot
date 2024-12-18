Проектом является контейнеризированный телеграмовский бот написанный на aiogram с базой данных на postgresql.
Бот позволяет:
1) Получить лучшее предложение в данный момент (выбирается по нескольким критериям: кол-во отзывов, рейтинг, ...) в категории Minecraft на сайте FunPay, и сохранить это предложение в базу. 
2) Выдаёт граф статистики о лучших предложениях за последнии дни пользования ботом.
Для работы проекта необходимо установить Docker Compose последней версии.
Для запуска достаточно запустить bash скрипт
```shell
chmod +x build.sh
./build.sh
```

Для отключения
```shell
docker compose down
```