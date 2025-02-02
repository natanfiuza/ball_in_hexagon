# Ball in Hexagon


Física da Bola Quicando: Explorando a Dinâmica em um Hexágono Giratório

## Descrição

Este projeto oferece uma exploração interativa e visualmente envolvente dos conceitos de física por meio de uma simulação em Python. Ele apresenta uma bola quicando dentro de um hexágono giratório, permitindo que os usuários observem e manipulem os princípios da dinâmica em ação.

A simulação, criada com o Pygame, representa realisticamente os efeitos da gravidade, do atrito e da restituição (elasticidade das colisões) no movimento da bola. Os usuários podem modificar esses parâmetros e ver em tempo real como eles influenciam a trajetória, a velocidade e o comportamento de quique da bola. Além disso, a rotação do próprio hexágono introduz um elemento adicional de complexidade, demonstrando como as forças e os quadros de referência interagem.

### Destaques educacionais

*   **Aprendizagem prática:** os usuários podem experimentar diretamente com variáveis como gravidade, atrito e restituição para obter uma compreensão intuitiva de seus efeitos.
*   **Representação visual:** a simulação fornece uma representação visual clara dos conceitos da física, tornando as ideias abstratas mais concretas.
*   **Exploração interativa:** os usuários podem fazer uma pausa, retroceder e até mesmo intervir manualmente no movimento da bola para testar hipóteses e aprofundar sua compreensão.
*   **Conexão com o código:** o código Python por trás da simulação é bem estruturado e comentado, permitindo que os usuários conectem os conceitos teóricos à sua implementação prática.
*   **Física do mundo real:** a simulação modela com precisão cenários do mundo real, como o comportamento de uma bola quicando em uma superfície em movimento ou dentro de um recipiente irregular.

### Possíveis casos de uso

*   **Ferramenta de ensino em sala de aula:** demonstre conceitos de física, como movimento de projéteis, conservação de energia, colisões e quadros de referência de uma forma envolvente e memorável.
*   **Aprendizagem individual:** permita que os alunos explorem os princípios da física em seu próprio ritmo, promovendo a curiosidade e a experimentação autodirigida.
*   **Projetos de ciências:** forneça uma plataforma para que os alunos projetem e conduzam experimentos virtuais, analisem dados e tirem conclusões.
*   **Introdução à programação:** sirva como um exemplo acessível de como a codificação pode ser usada para modelar fenômenos físicos, inspirando interesse na ciência da computação.

### Recursos adicionais

*   A simulação pode ser aprimorada com recursos como:
    *   Exibição de gráficos de vetores de velocidade e força.
    *   Rastreamento e plotagem de caminhos de energia cinética e potencial.
    *   Permitindo que os usuários ajustem a velocidade de rotação do hexágono.
    *   Introdução de vários balanços com interações.
*   Um tutorial ou guia que acompanha pode explicar os conceitos da física por trás da simulação, orientar os usuários em experimentos e fornecer insights sobre o código Python.

No geral, este projeto serve como uma ferramenta educacional valiosa, combinando o poder da simulação interativa com a clareza do código Python para tornar o aprendizado da física uma experiência envolvente e esclarecedora.

## Prompt utilizado

A partir de um prompt foi criado um programa onde uma bola quica dentro de hexagono que gira.
Este prompt aseguir foi aplicado em 5 (cinco) IA generativas mais populares no momento, são elas `ChatGPT`, `Gemini`, `DeepSeek`, `Qwen Chat` e `Claude`.

```text

Escreva um programa Python que mostre uma 
bola quicando dentro de um hexágono giratório. 
A bola deve ser afetada pela gravidade e pelo 
atrito, e deve quicar nas paredes giratórias 
de forma realista.

```

## IAs generativas

Você pode ver a resposta de cada IA aqui:

* [ChatGPT](./chatgpt.md)
* [Gemini](./gemini.md)
* [DeepSeek](./deepseek.md)
* [Qwen Chat](./qwenchat.md)
* [Claude](./claude.md)


## Dependências

Este projeto utiliza as seguintes bibliotecas Python para a criação da simulação:

*   **Pygame:**  Uma biblioteca amplamente utilizada para o desenvolvimento de jogos e aplicações multimídia em Python. No contexto deste projeto, o Pygame é empregado para:
    *   **Criação da janela de exibição:**  Gerenciar a janela onde a animação será renderizada.
    *   **Renderização gráfica:** Desenhar os elementos visuais da simulação, como a bola e o hexágono.
    *   **Controle de eventos:**  Lidar com eventos do teclado e mouse, caso a simulação possua interatividade.
    *   **Manipulação de tempo:** Controlar a taxa de atualização da animação (FPS).

    Você pode encontrar mais informações sobre o Pygame em: [https://www.pygame.org/](https://www.pygame.org/)

*   **NumPy:** Uma biblioteca fundamental para computação científica em Python. O NumPy é utilizado neste projeto para:
    *   **Operações matemáticas:** Realizar cálculos vetoriais e matriciais, essenciais para a movimentação da bola e rotação do hexágono.
    *   **Eficiência numérica:**  O NumPy oferece estruturas de dados e funções otimizadas que tornam as operações matemáticas mais rápidas e eficientes, o que é crucial para uma animação fluida.

    Para saber mais sobre o NumPy, visite: [https://numpy.org/](https://numpy.org/)

### Observação sobre a Instalação

Conforme detalhado na seção [Instalação](#instalação), este projeto utiliza o `pipenv` para o gerenciamento de dependências. Ao executar o comando `pipenv install` (ou `pipenv install --dev` se desejar as dependências de desenvolvimento), o `pipenv` irá **automaticamente instalar o Pygame, NumPy e quaisquer outras dependências listadas no arquivo `Pipfile`** dentro do ambiente virtual do projeto. Portanto, você **não precisa** instalar essas bibliotecas manualmente.

Caso não esteja utilizando o `pipenv`, será necessário instalar as dependências manualmente usando o `pip`, por exemplo:

```bash
pip install pygame numpy
```
No entanto, **recomenda-se fortemente o uso do `pipenv`** para garantir a consistência do ambiente e evitar conflitos de dependências com outros projetos Python em seu sistema.

-----

## Instalação

Este projeto utiliza o `pipenv` para gerenciar as dependências. 

Siga os passos abaixo para instalar e configurar o ambiente de desenvolvimento:

### Pré-requisitos

*   Python 3.x (recomendado Python 3.11 ou superior)
*   `pip`
*   `pipenv`

### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone git@github.com:natanfiuza/ball_in_hexagon.git
    cd ball_in_hexagon
    ```

2.  **Instale as dependências usando o `pipenv`:**

    ```bash
    pipenv install
    ```
    Este comando irá criar um ambiente virtual e instalar todas as dependências listadas no arquivo `Pipfile`.

3.  **Ative o ambiente virtual:**

    ```bash
    pipenv shell
    ```
    Isso ativará o ambiente virtual criado pelo `pipenv`. Todos os comandos a seguir devem ser executados dentro desse ambiente.

4.  **(Opcional) Instale as dependências de desenvolvimento:**

    Se você precisar das dependências de desenvolvimento (por exemplo, para testes), use:

    ```bash
    pipenv install --dev
    ```

**Pronto!** Agora você já pode executar o programa (veja a seção "Utilização" para mais detalhes).



## Utilização

Este projeto contém 5 scripts Python, cada um gerando um programa que simula uma bola quicando dentro de um hexágono giratório. Cada script foi criado por uma IA diferente:

*   `chatgpt.py` (criado por ChatGPT)
*   `gemini.py` (criado por Gemini)
*   `deepseek.py` (criado por DeepSeek)
*   `qwenchat.py` (criado por Qwen Chat)
*   `claude.py` (criado por Claude)

**Para executar os programas, siga os passos abaixo:**

**Certifique-se de que você já tenha concluído a instalação conforme descrito na seção [Instalação](#instalação).**

1.  **Ative o ambiente virtual:**

    ```bash
    pipenv shell
    ```

2.  **Execute cada um dos scripts individualmente:**

    Para rodar a simulação gerada por cada IA, execute o script correspondente usando o comando `python`. Por exemplo:

    ```bash
    python chatgpt.py
    ```

    ```bash
    python gemini.py
    ```

    ```bash
    python deepseek.py
    ```

    ```bash
    python qwenchat.py
    ```

    ```bash
    python claude.py
    ```

    Cada comando abrirá uma nova janela exibindo a simulação da bola quicando dentro do hexágono giratório.

**Observações:**

*   Cada script é independente e gera uma versão única da simulação, refletindo as nuances de cada IA que o criou.
*   Você pode fechar a janela da simulação para encerrar a execução de cada script.
*   Caso encontre algum erro, verifique se o ambiente virtual está ativado e se todas as dependências foram instaladas corretamente (consulte a seção [Instalação](#instalação)).

**Dicas:**

*   Você pode executar os scripts em diferentes terminais/janelas para comparar as animações lado a lado.

**Aproveite a visualização das diferentes implementações da simulação criadas pelas IAs!**


## Considerações Finais e Agradecimentos

Este projeto foi desenvolvido como um experimento para explorar as capacidades de diferentes IAs na criação de código Python para uma simulação visual. Através dos 5 scripts gerados - `chatgpt.py`, `gemini.py`, `deepseek.py`, `qwenchat.py` e `claude.py` - podemos observar as diferentes abordagens e estilos de codificação empregados por cada uma delas, resultando em variações sutis na animação da bola quicando dentro de um hexágono giratório.

### Sugestões e Uso Didático

Este projeto é especialmente recomendado para **uso didático** por estudantes que estão aprendendo a linguagem Python. Ele oferece uma oportunidade única de:

*   **Comparar Diferentes Estilos de Código:** Analisar os scripts gerados por cada IA permite que os alunos observem diferentes maneiras de estruturar o código, utilizar bibliotecas gráficas (se houver) e implementar a lógica da simulação.
*   **Compreender o Processo de Criação de Código por IAs:** O projeto serve como um exemplo prático de como as IAs podem ser usadas para auxiliar no desenvolvimento de software, gerando código funcional a partir de descrições textuais.
*   **Aprender na Prática Conceitos de Animação e Geometria:** Os alunos podem estudar como a animação da bola e a rotação do hexágono são implementadas no código, reforçando conceitos de geometria e movimento em um contexto visualmente atrativo.
*   **Modificar e Expandir o Código:** Os scripts servem como um ponto de partida para experimentação. Os alunos são encorajados a modificar o código, alterar parâmetros, adicionar novos elementos e explorar diferentes comportamentos da simulação.

### Agradecimentos

Agradeço às equipes por trás das IAs que contribuíram para este projeto: ChatGPT (OpenAI), Gemini (Google), DeepSeek, Qwen Chat (Alibaba) e Claude (Anthropic). A capacidade dessas IAs de gerar código funcional é impressionante e abre um leque de possibilidades para o futuro do desenvolvimento de software.

### Contribuições e Contato

Contribuições para este projeto são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou ideias para expandir a simulação, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* neste repositório.

Para qualquer dúvida, sugestão ou feedback, entre em contato:

**Natan Fiuza**

**Email:** [contato@natanfiuza.dev.br](mailto:contato@natanfiuza.dev.br)

Espero que este projeto seja útil e inspirador para estudantes e entusiastas da programação Python!