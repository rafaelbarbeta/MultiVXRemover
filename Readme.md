# MultiVXRemover

## Conceito do projeto
Projeto de mini-antívirus, que consegue detectar assinaturas de malwares conhecidos assim como colocá-los em "quarentena". Foi feito inteiramente em python com ajuda da biblioteca de regras YARA. Adicionalmente,inclui uma breve pesquisa sobre o vírus de computador conhecido como Neshta, com sua análise dinâmica e estática.

Todos os softwares desenvolvidos contém padrões exclusivos, que permitem indentificá-los em meio a tantos outros. O mesmo acontece com malwares. Um dos mecanismos mais úteis dos antivírus modernos é justamente a detecção por assinatura, que consiste em catalogar diversos desses "padrões" de antivírus em uma base de dados e compará-los com os arquivos presentes no computador do usuário. Um "match" provavelmente significa que aquele arquivo é um malware já conhecido e que portando desve ser isolado pela segurança do cliente.

Dois tipos de assinatura são utilizados para detecção de software maliciosos nesse projeto:
* Regras YARA: consiste em um conjunto de expressões regulares aplicadas ao binário. Consegue dar "match" tanto em bytes "raw", strings de texto e combinar os diferentes "matches" que ocorreram com expressões lógicas. É o mecanismo principal de detecção. Consegue detectar malwares e possíveis "variantes" desse software malicioso. 
* Hash MD5: O hash é como uma "somatório do conteúdo de um arquivo". A função hash, no caso o MD5, recebe um arquivo de tamanho arbitrário e produz uma string fixa que é potencialmente exclusiva para esse arquivo. É bastante inflexível, uma mínima alteração muda completamente o hash, sendo muito específica para indetificar um sofware único. A vantagem é que apenas softwares já catalogados com esse hash serão efetivamente detectados, com menor probabilidade de um "match" errôneo

O projeto inclui um set de regras YARA obtidos da Reversing LABS. O projeto original pode ser encontrado [nesse link](https://github.com/reversinglabs/reversinglabs-yara-rules)

Além disso, inclui um "scraper" downloader.sh para hashes MD5 do site vírus share. Há uma coleção **gigantesca** de assinaturas de vírus coletadas da internet. O download de todos os arquivos pode demorar algum tempo, mas se desejar, adicione sesu próprios hashes para teste.
  
## Pré-requisitos e recursos utilizados
Citação das linguagens, bibliotecas, peças de hardware, e outras coisas que o grupo utilizou para realizar o projeto. Não é necessário explicar qual foi o uso exato de cada coisa no projeto. Bibliotecas e recursos padrões das tecnologias utilizadas não precisam ser citados (ex: stdio.h, iostream.h, etc.).

Se alguma biblioteca externa ou código de outra pessoa foi utilizado como recurso, é importante citar a fonte de onde vocês retiraram (pode ser o link no Github, ou tutorial usado como referência).

### Exemplo:

O grupo utilizou a linguagem C para desenvolver a implementação geral do projeto, além de importar as seguintes bibliotecas:
1. abcdzd.h
2. exemplo.h, disponível em [IstoEhApenasUmExemplo](https://github.com/istoehapenasumexemplo/minhabiblioteca)

Também foi utilizado o tutorial disponível em [IstoEhOutroExemplo](https://github.com/istoehoutroexemplo/oi) como base para o grupo compreender a implementação da função X dentro da linguagem em questão.
  
## Passo a passo
Passos que o grupo realizou para criar, implementar ou projetar o projeto. É importante descrever pelo menos o mais importante para que outras pessoas compreendam como o grupo conseguiu realizar o projeto, quais as atividades feitas, etc, e possam ter meios compreender como reproduzir o projeto, se assim fosse necessário.

Se possível, é legal citar o nome dos arquivos implementados, se forem poucos. Por exemplo, se o seu projeto tiver 4 arquivos, cada um com uma função, citar o nome deles na parte do passo a passo correspondente. Se forem muitos arquivos para uma mesma coisa, não tem problema, podem deixar sem ou deixar apenas o nome da pasta.

### Exemplo:

1. Baixamos o material disponível em [Material](https://materialdeexemplodohackerspace.com.br)
2. Estudamos como o código do material anterior funciona
3. Implementamos um programa que se comunicasse com o código compreendido (comunicacao.c e comunicacao.h)
4. Implementamos uma interface gráfica para utilizar o programa de comunicação de forma mais intuitiva.

## Instalação
Passos necessários para instalar ou recriar seu projeto, se assim for necessário. A descrição dos passos não precisa ser complexa. É necessário apenas o mais importante para que outras pessoas saibam como fazê-lo.

### Exemplos:
a)
  ```
  Execute o comando X Y Z, no terminal, na pasta do projeto
  ```
b)
  1. Abra a pasta 
  2. Execute o comando A B C no terminal
  3. Compile os arquivos X, Y e Z juntos
  4. Crie um arquivo W.txt de entrada

## Execução
Passos necessários para executar, rodar ou testar seu projeto. Vocês podem seguir o mesmo modelo dos exemplos de Instalação.

## Bugs/problemas conhecidos
Por ter sua detecção baseado apenas em assinaturas, o MultiVXRemover não é capaz de detectar os chamados malwares metamórficos/polimórfimos ou ameaças recentes. De forma resumida, malwares que mudam sua forma (sua assinatura) "espontaneamente" ou que acabaram de serem criados não serão detectados por regras estáticas, que ficam muito limitadas aos softwares que as deram origem. Soluções de antivírus modernas incluem análise heurística e em tempo real da atividade de cada software no PC, se concentrando mais **na ação** do programa do que no **seu código**. 

A compilação das regras YARA geralmente será rápida, porém, o download e criação do banco de dados SQL dos hashes pode levar algum tempo, cerca de 30 minutos. A detecção com hashes também sofre do mesmo problema, demorando relativamente bastante tempo para comparação do hash de um arquivo com o banco de dados. Tentativas de otimização foram feitas para acelerar o processo, sendo que a organização em banco de dados sqlite foi a mais promissora.

## Autores
* [Rafael Barbeta](https://github.com/rafaelbarbeta)
* [Victor Motta](https://github.com/maxproyt)

## Demais anotações e referências (opcional)
Encoraja-se fortemente o uso dessa ferramenta em um ambiente controlado e seguro como uma máquina virtual. Esse projeto NÃO substitue uma antivírus profissional. Os criadores não serão responsáveis por quaisqueres incidentes que ocorram devido ao uso desse software.

## Imagens/screenshots
É necessário colocar pelo menos 3 imagens/screenshots do projeto, porém fiquem a vontade para colocar mais, a medida do que vocês acharem legal para ilustrar o projeto.

Para colocar imagens no Readme do Github, vocês podem usar o seguinte comando (abrir este Readme no modo raw ou como txt):

![Imagem](https://github.com/hackoonspace/Hackoonspace-template/blob/master/exemplo.png)

É preferível que vocês usem imagens hospedadas no próprio GitHub do projeto. É só referenciar o link delas no comando acima.
