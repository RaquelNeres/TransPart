# TransPart
site para fazer a manipulaçõa de partituras

[Explicação Flask](https://www.freecodecamp.org/portuguese/news/como-criar-uma-aplicacao-da-web-usando-o-flask-e-implanta-la-na-nuvem/)

# Por Que Usamos Essas Bibliotecas no Projeto?

Este documento explica a escolha e o papel de cada biblioteca no nosso projeto de análise musical e geração de partituras.

## O Problema: Duas Tarefas, Duas Ferramentas

Nosso projeto precisa resolver dois desafios distintos na área de processamento musical:

1. **Analisar arquivos de áudio** para extrair informações musicais
2. **Manipular e gerar partituras** digitais

Para isso, escolhemos duas bibliotecas especializadas que se complementam perfeitamente.

## Librosa: A Ferramenta de Análise de Áudio

### O que faz
A `librosa` é nossa biblioteca principal para **análise de áudio**. Ela funciona como um "ouvido digital" que consegue processar arquivos de áudio (`.mp3`, `.wav`, `.flac`, etc.) e extrair informações musicais complexas.

### Por que escolhemos
- **Detecção de altura (pitch)**: Identifica as frequências das notas tocadas
- **Análise temporal**: Detecta ritmo, tempo e duração das notas
- **Separação de componentes**: Consegue isolar melodia do acompanhamento
- **Robustez**: Funciona bem mesmo com gravações que têm ruído ou múltiplos instrumentos

### Exemplo de uso no projeto
```python
import librosa
# Carrega o áudio e extrai as frequências fundamentais
y, sr = librosa.load('audio.wav')
pitches = librosa.yin(y, fmin=80, fmax=400)
```

## Partitura: A Ferramenta de Notação Musical

### O que faz
A biblioteca `partitura` é nossa ferramenta para **manipulação de partituras digitais**. Ela não processa áudio, mas trabalha com a representação simbólica da música (notas, ritmos, armaduras, etc.).

### Por que é essencial
- **Criação de partituras**: Transforma os dados do `librosa` em notação musical padrão
- **Transposição**: Permite mudar o tom da música facilmente
- **Exportação**: Gera arquivos MusicXML e MIDI que podem ser lidos por outros softwares
- **Edição musical**: Adiciona, remove ou modifica elementos da partitura

### Exemplo de uso no projeto
```python
import partitura
# Cria uma partitura a partir dos dados extraídos do áudio
score = partitura.Score()
# Transpõe a música para um tom diferente
transposed = partitura.transpose(score, semitones=2)
```

## Como Elas Trabalham Juntas

O fluxo do nosso projeto funciona assim:

```
Arquivo de Áudio → librosa → Dados Musicais → partitura → Partitura Digital
```

### Etapa 1: Análise (Librosa)
O `librosa` recebe o arquivo de áudio e extrai:
- Frequências das notas
- Duração de cada nota
- Informações de ritmo e tempo

### Etapa 2: Síntese (Partitura)
O `partitura` recebe esses dados e:
- Converte frequências em notas musicais (Dó, Ré, Mi...)
- Organiza as durações em figuras rítmicas (semínimas, colcheias...)
- Gera a partitura final em formato padrão

## Funcionalidades Específicas do Projeto

### Conversão Áudio → Partitura
- **Librosa**: Detecta as notas tocadas no áudio
- **Partitura**: Organiza essas notas em uma partitura legível

### Transposição Musical
- **Apenas Partitura**: Modifica o tom da música sem perder a qualidade
- **Por que não Librosa**: Alterar áudio digitalmente introduz artefatos e perda de qualidade

### Edição de Partituras
- **Apenas Partitura**: Adiciona ou remove notas, muda armaduras de clave
- **Por que não Librosa**: Trabalha apenas com análise, não com criação

## Analogia Final

Pense nas bibliotecas como ferramentas complementares:

- **Librosa** é como um **microfone inteligente**: "escuta" o áudio e te diz o que está acontecendo musicalmente
- **Partitura** é como uma **máquina de escrever musical**: pega essas informações e cria uma partitura organizada e editável

Ambas são necessárias porque resolvem problemas diferentes no mesmo domínio musical, e juntas permitem criar um sistema completo de análise e síntese musical.