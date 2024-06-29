# Como configurar/instalar/usar a `taskbar` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar a `taskbar` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install the `taskbar` on `Linux Ubuntu`._

## Descrição [2]

### `taskbar`

A `"taskbar"` ou barra de tarefas, é uma componente crucial do ambiente de área de trabalho em sistemas operacionais como o Ubuntu e o Windows. Localizada geralmente na parte inferior da tela, ela proporciona acesso rápido a aplicativos em execução, bem como a janelas abertas, tornando a navegação e a multitarefa mais convenientes. Além disso, a `"taskbar"` exibe informações essenciais, como a hora e o status do sistema, e muitas vezes inclui um menu de aplicativos ou botão Iniciar para facilitar o lançamento de novos programas e acesso às configurações do sistema. Essa funcionalidade central na interface do usuário do sistema operacional ajuda os usuários a gerenciar eficazmente suas tarefas e a interagir com seus computadores de forma eficiente.

## 1. Como configurar/instalar/usar a `taskbar` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar a `taskbar` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    

3. Abrir o `whiskermenu`;

4. Digitar `panel` e clicar na tecla `Enter`

5. Clicar na aba `Items`;

6. Selecionar a opção `Windows Buttons`;

7. Clicar em `Edite the currente selected item`;

8. em `Appearance`, remover o `check` do `Show button labels`; [3]

9. Em `Behaviour`, no campo `Window grouping`, selecione a opção ` Always`. [2]

### 1.1 Código completo para configurar/instalar

Para configurar/instalar/usar o `taskbar` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÂO há.
    ```


## Referências

[1] OPENAI. ***Desktop environment that stacks programs in the task bar.*** Disponível em: <https://unix.stackexchange.com/questions/224246/desktop-environment-that-stacks-programs-in-the-task-bar> (texto adaptado). StackExchange. Acessado em: 22/12/2023 11:35.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 22/12/2023 11:36.

[3] DK BOSE. ***How can i get icon only "grouped modern window list" on xubuntu, that I can "pin" in panel too?.*** Disponível em: <https://askubuntu.com/questions/1173886/how-can-i-get-icon-only-grouped-modern-window-list-on-xubuntu-that-i-can-pin> (texto adaptado). StackExchange. Acessado em: 22/12/2023 11:37.

