#!/bin/sh

output=$(gh auth status 2>&1)

echo "Output: $output"

if echo "$output" | grep -q "You are not logged into any GitHub hosts. To log in, run: gh auth login"; then
    gh auth login
else
    gh auth setup-git 
    git config --global user.name "Askodon"
    git config --global user.email "askodon@disroot.org"
    git config --global core.editor "nvim"
    gitui
fi
