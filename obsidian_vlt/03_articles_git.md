
# GIT

git config --global http.ssl backend schannel

```
git clone <repo_link.git>


git pull
git status
git checkout <branch>
git branch -a
git branch <branch>
git push -u origin <branch>
```
Удаление ветки в удаленном репозитории
```
git push origin --delete <branch>
```
удаление ветки в локальном репозитории
```
git branch -d <branch>
```

Добавление всех изменений в origin
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
git log


###  Склейка коммитов

Посмотреть какие коммиты нужно склеить. Какие коммиты прибавились по сравнению с веткой master
git cherry -v master
Посчитать сколько таких коммитов. Количество потребуется далее.
git cherry -v master | wc -l
Переписать историю за N коммитов. Сколько именно, выяснили ранее. Команда откроет редактор, где перед каждым коммитом стоит метка что с ним сделать. Простой способ: первому поставить pick, остальным - squash. После сохранения этого изменения, откроется редактор для ввода сообщения коммита.
git rebase -i HEAD~N
Теперь отправляем изменения на origin 
git push --force


