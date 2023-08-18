# Отправляем фотографии космоса в Telegram

Это модули, которые скачивают, а потом отправляю фотографии космоса в Telegram-канал

### Как установить

1. Создайте файл .env и добавьте токен, полученный из [Nasa](https://api.nasa.gov/). Также добавьте токен Вашего бота и ID канала, куда бот будет отправлять картинки. Вот пример:
```
NASA_TOKEN=[Ваш Nasa токен]
TG_TOKEN=[Токен бота]
CHAT_ID=[ID канала]
```

2. Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```powershell
pip install -r requirements.txt
```


### Как запустить

1. Скачайте картинки
  - Скачиваем фотографии Земли из космоса: 
  ```powershell
  python ./get_epic_images.py 
  ```
  - Скачиваем фотографии про космос, которые сегодня популярны: 
  ```powershell
  python ./get_day_images.py
  ```
  - Скачиваем фотографии с запуска ракет SpaceX(параметром -i указываем ID запуска, а если он не указан, то скачиваются фотографии последнего запуска): 
  ```powershell
  python ./fetch_spacex_images.py -i 5eb87d47ffd86e000604b38a
  ```

2. Запускаем бота
  - Можно оправить все фотографии из images с задержкой(можем указать в параметре -d задержку между фотографиями, а если не указана, то используются данные из .env): 
  ```powershell
  python ./telegram_bot.py -d 5
  ```
  - Можно отправить один файл из images(Можно указать параметр -p: название фотографии, а если параметр не указан, то выберется случайная фотография и тоже отправится): 
  ```powershell
  python ./publish_photo.py -p test.jpg
  ```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
