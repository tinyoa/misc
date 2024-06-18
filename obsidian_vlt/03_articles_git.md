
# GIT


## Конфигурация



```
git config user.name username
git config user.email username@mail.com
```

```
git config --global http.ssl backend schannel
```


```
git clone <repo_link.git>

git pull
git status
git checkout <branch>
git branch -a
git branch <branch>
git push -u origin <branch>
```

#### Конфигурация github
Чтобы добиться аутентификации из termux потребовалось использовать персональные токены  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens


## Удаление ветки
Удаление ветки в удаленном репозитории
```
git push origin --delete <branch>
```
удаление ветки в локальном репозитории
```
git branch -d <branch>
```

## Добавление всех изменений в origin
```
git add .
git commit -m "<commit message>"
git push
```

добавить в агент ключ
```
$ eval $(ssh-agent -s)
$ ssh-add c:/Users/User/key
```

Просмотреть лог
```
git log
```


###  Склейка коммитов

Посмотреть какие коммиты нужно склеить. Какие коммиты прибавились по сравнению с веткой master
```
git cherry -v master
```
Посчитать сколько таких коммитов. Количество потребуется далее.
```
git cherry -v master | wc -l
```
Переписать историю за N коммитов. Сколько именно, выяснили ранее. Команда откроет редактор, где перед каждым коммитом стоит метка что с ним сделать. Простой способ: первому поставить pick, остальным - squash. Если есть чужие коммиты им можно поставить  drop. После сохранения этого изменения, откроется редактор для ввода сообщения коммита.
```
git rebase -i HEAD~N
```
Теперь отправляем изменения на origin 
```
git push --force
```


### Добавление ssh-ключей в git bash

```
$ eval $(ssh-agent -s)
$ ssh-add c:/Users/UsernaME/key
```


### Пробую, но пока не уверен

##### Your branch is ahead of 'origin/branch' by 2 commits
локальная ветка опережает ветку на сервере на 2 коммита. 
Чтобы отбросить свои изменения делаем сброс:
```
git reset --hard origin/branch
```

