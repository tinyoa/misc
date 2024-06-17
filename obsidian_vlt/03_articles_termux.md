


#### Доступ к внешнему и внутреннему хранилищу

Для того, чтобы получить доступ к внутреннему (общему) или внешнему хранилищу, необходимо выполнить команду .


При выполнении `termux-setup-storage` происходит следующее:
1. Будет запрошено разрешение на доступ к хранилищу.
2. Termux создаст приватную директорию во внешнем и внутреннем хранилищах.
3. Создаст директорию $HOME/storage в которой будут символьные ссылки на приватные директории приложения, а также ссылки на стандартные директории Android OS.

путь `/data/data/com.termux/files/home/storage/shared`

#### git 

##### ERRORS

###### fatal: detected dubious ownership
 **Git не может определить, кто владеет файлами в репозитории**.
Это может произойти по разным причинам, например:
- если вы клонировали репозиторий из публичного источника и не установили правильные разрешения на владение;
- если вы случайно удалили файлы, содержащие информацию о владельце.
Чтобы исправить ошибку, можно изменить владельца репозитория на пользователя, который клонировал репозиторий, или удалить репозиторий и клонировать его снова из частного источника.

```
fatal: detected dubious ownership in repository at '/storage/emulated/0/Documents/misc'
$ git config --global --add safe.directory /storage/emulated/0/Documents/misc
```


### ssh

```
pkg upgrade
pkg install openssh 
```

``` ssh-keygen -t rsa -b 2048 -f id_rsa ```
команда сгенерирует файлы id_rsa и id_rsa.pub в директории /data/data/com.termux/files/home


### Структура хранилища

```
data/data/com.termux/files/
  |-home
    id_rsa
    id_rsa.pub
    |-storage
      |-dcim
      |-downloads
      |-movies
      |-music
      |-pictures
      
  |-usr
    |-bin
    |-etc
    |-include
    |-lib
    |-libexec
    |-share
    |-tmp
    |-var
```