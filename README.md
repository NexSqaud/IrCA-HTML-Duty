# IrCA HTML Duty

Поддерживает все сигналы (даже будущие), может использоваться множеством пользователей и не требует получения токенов!

## Установка на pythonanywhere
Для установки мы будем использовать сайт [pythonanywhere.com](https://www.pythonanywhere.com/)

Переходим по [ссылке](https://www.pythonanywhere.com/registration/register/beginner/), заполняем форму и нажимаем *Register*

*(Под словами "вкладка X" далее по тексту, имеются в виду ссылки на этой панели)*
[![](https://sun9-35.userapi.com/GvwS8jmduczHApabBhlJyeJcAzhMLkFEE8Bqmw/_UZT_5jUQtk.jpg)](https://sun9-35.userapi.com/GvwS8jmduczHApabBhlJyeJcAzhMLkFEE8Bqmw/_UZT_5jUQtk.jpg)


Далее открываем вкладку *Web*
Кликаем на *Add a new web app*
В появившемся окошке *next*  -> *Flask* -> *Python3.8*\
В путь вводим /home/`имя аккаунта`/IrCA-HTML-Duty/duty.py

Тыкаем на вкладку *Consoles*. Ищем блок *Start a new console*, в нем выбираем *Bash*

После загрузки набираем в консоли
(это две команды, после каждой нужно нажимать Enter)
```bash
rm -rf IrCA-HTML-Duty
git clone --branch PythonAnywhere https://github.com/NexSqaud/IrCA-HTML-Duty
```

Далее переходим во вкладку *Web* и нажимаем на кнопку *Reload* `имя аккаунта`.pythonanywhere.com

Отправляем ирису следующую фразу (имя_аккаунта - логин на pythonanywhere):
```
+api *секретная фраза* http://имя_аккаунта.pythonanywhere.com
```
Готово!