# Knowledge Base

Repository for saving my code snippets for future reference.

## Git Config

`git config --global user.name "Thales Barreto"`

`git config --global user.email "trvbarreto@gmail.com"`

`git config --global init.defaultBranch main`

`git config --global color.ui auto`

`git config --get user.name`

`git config --get user.email`

Após isso, configurar chave SSH

`ssh-keygen -t ed25519 -C trvbarreto@gmail.com`

`cat ~/.ssh/id_ed25519.pub`

`ssh -T git@github.com`
