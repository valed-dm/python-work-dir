В папке app/db/psql_cred.py данные для подключения к БД postgresql:

postgresql = {
'pguser': 'dmitrijvaledinskij',
'pgpasswd': '',
'pghost': 'localhost',
'pgport': 5432,
'pgdb': 'menus'
}

Для запуска проекта в терминале:

    $ zsh,bash run.sh
    $ alembic upgrade head

Создается БД menus с таблицами menus, submenus, dishes.
Приложение готово к работе и тестированию.
