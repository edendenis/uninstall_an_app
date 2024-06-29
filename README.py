#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `desinstalar uma aplicação` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `desinstalar uma aplicação` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `uninstall an application` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `application`
# 
# Uma aplicação, ou _software_ aplicativo, refere-se a um programa de computador projetado para realizar tarefas específicas e resolver necessidades dos usuários. Essas tarefas podem variar amplamente, desde processamento de texto e planilhas até navegação na web, jogos, edição de imagens, entre outros. As aplicações são desenvolvidas para serem executadas em sistemas operacionais específicos, como Windows, macOS, Linux, Android ou iOS, e podem ser distribuídas tanto comercialmente quanto de forma gratuita.
# 

# ## 1. Como configurar/instalar/usar o `desinstalar uma aplicação` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar a `desinstalar uma aplicação` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para desinstalar uma aplicação no `Linux Ubuntu`, você pode usar o comando `apt-get` ou `dpkg`, dependendo de como você instalou o programa inicialmente. Aqui estão os passos para desinstalá-lo:
# 
# ### 1.1 Usando `apt-get`
# 
# 1. Se você instalou o 4K Video Downloader usando o apt-get, use o seguinte comando: `sudo apt-get remove <nome_da_aplicacao>`
# 
# 2. Para remover também os arquivos de configuração, use: `sudo apt-get purge <nome_da_aplicacao>`
# 

# ### 1.2 Usando `dpkg`
# 
# 1. Se você instalou a aplicação usando um pacote `.deb`, você pode removê-lo com o seguinte comando: `sudo dpkg -r <nome_da_aplicacao>`
# 
# 2. Para remover completamente, incluindo arquivos de configuração, use: `sudo dpkg --purge <nome_da_aplicacao>`
# 

# 1.3 Usando `apt`
# 
# 1. Outra maneira de remover o pacote é usar o comando `apt`: `sudo apt remove <nome_da_aplicacao>`
# 
# 2. Para remover completamente, incluindo arquivos de configuração, use: `sudo apt purge <nome_da_aplicacao>`
# 

# In[ ]:


## 2. Autoclean e Autoremove

1. Após desinstalar o programa, é uma boa prática limpar pacotes não utilizados:

```
sudo apt-get autoremove
sudo apt-get autoclean
```

Isso removerá a aplicação do seu sistema `Linux Ubuntu`.


# ### 3. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `desinstalar uma aplicação` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Desinstalar uma aplicação do linux ubunru.*** Disponível em: <https://chatgpt.com/c/7eccedfc-836d-4e28-a696-be591ae9435f> (texto adaptado). StackExchange. Acessado em: 22/12/2023 11:35.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 22/12/2023 11:36.
# 
