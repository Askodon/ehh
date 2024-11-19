#!/bin/sh

# Выполняем команду и сохраняем вывод в переменную
output=$(gh auth status 2>&1)  # Перенаправляем ошибки в стандартный вывод

# Выводим отладочную информацию
echo "Вывод команды: $output"

# Проверяем, содержит ли вывод нужное сообщение
if echo "$output" | grep -q "You are not logged into any GitHub hosts. To log in, run: gh auth login"; then
    # Если сообщение найдено, выполняем команду "gh auth login"
    echo "Выполняем команду для входа в GitHub..."
    gh auth login
else
    # Если сообщение не найдено, выводим результат команды
    gh auth setup-git 
    git config --global user.name "Askodon"
    git config --global user.email "askodon@disroot.org"
    git config --global core.editor "nvim"
    gitui
fi
