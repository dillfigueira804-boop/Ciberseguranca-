# 🛡️ AI Guardrail: Detector de Indirect Prompt Injection em PDFs

Projeto prático desenvolvido durante a formação **Agentes de IA do Zero à Prática (DIO)**, focado em segurança para Modelos de Linguagem (OWASP Top 10 for LLMs - LLM01: Prompt Injection).

## 📌 O Problema
Sistemas e Agentes de IA que analisam documentos externos (como currículos em sistemas de RH ou petições em tribunais) não "enxergam" a página visualmente — eles extraem o texto bruto do arquivo. Pessoas mal-intencionadas aproveitam essa característica inserindo comandos ocultos (texto em **cor branca** e tamanho reduzido) para manipular a decisão do agente.

## 💡 A Solução (Agente Guardrail v3)
Desenvolvi um **Agente Guardrail em Python** (`Untitled2.ipynb`) utilizando a biblioteca `pypdf` que realiza uma auditoria dupla antes de liberar o documento para o modelo de linguagem principal:

1. **Inspeção Forense de Stream PDF:** Analisa a estrutura interna do arquivo em busca de definições de cor branca (`1 1 1 rg` / `1.0 1.0 1.0 rg`), capturando textos ocultos mesmo quando formatados em tamanhos legíveis (como `8pt` em editores mobile).
2. **Análise Semântica de Gatilhos:** Varre o texto extraído em busca de padrões clássicos de sequestro de instrução (*System Override*, *Ignore instruções anteriores*, etc.).

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Google Colab** (Ambiente de desenvolvimento e simulação)
* **PyPDF & FPDF** (Geração de PDFs de teste, extração de texto e auditoria interna)

## 🚀 Como Testar
Clique no selo **"Open in Colab"** dentro do arquivo `Untitled2.ipynb` deste repositório e execute as células para simular um currículo com ataque de injeção e vê-lo ser bloqueado em tempo real (`🚨 STATUS: BLOQUEADO`).




## 🛠️ Novos Aprendizados (Estudos Autodidatas via IA e Google)

### 🔑 Gerador de Senhas Seguras (`gerador_senhas.py`)
* **Módulo Secrets:** Entendi que para segurança não se usa o `random` comum, mas sim a biblioteca `secrets`, que gera dados imprevisíveis e criptograficamente seguros.
* **Garantia de Regras:** Lógica estruturada para forçar a inclusão de letras maiúsculas, minúsculas, números e caracteres especiais, conversando com o validador de senhas.

### 🛡️ Verificador de Integridade (`verificador_integridade.py`)
* **Pilar da Integridade:** Estudo prático da letra **I** da Tríade CIA, garantindo que arquivos ou mensagens não foram alterados por terceiros.
* **Efeito Avalanche:** Observação de como a mudança de uma única letra altera completamente a assinatura digital (Hash SHA-256) gerada pela biblioteca `hashlib`.

*Nota: Códigos estruturados e analisados com o auxílio de IA no ambiente Pydroid 3 para consolidação de conceitos teóricos de segurança da informação.*


# 🛡️ Detector de Fraudes Bancárias com Machine Learning

Simulação de um sistema de prevenção a fraudes em cartões de crédito utilizando **Python**, **Pandas** e **Scikit-Learn** (Árvore de Decisão), desenvolvido para identificar transações suspeitas em tempo real com base no valor e horário da compra.

## 🎯 Contexto do Problema
Regras manuais fixas (ex: bloquear qualquer compra acima de determinado valor) costumam gerar dois problemas críticos no setor financeiro:
1. **Falsos Positivos:** Bloqueio indevido de clientes legítimos fazendo compras de alto valor durante o dia.
2. **Falsos Negativos:** Falha em detectar golpistas testando cartões clonados com valores baixos durante a madrugada.

## 🛠️ Tecnologias Utilizadas
* **Python 3** (Google Colab)
* **Pandas:** Estruturação e manipulação da base histórica de transações.
* **Scikit-Learn (`DecisionTreeClassifier`):** Treinamento do modelo preditivo e visualização das regras de decisão.
* **Matplotlib:** Plotagem da árvore de decisão para explicabilidade do modelo (*Explainable AI*).

## 🔍 Evolução do Modelo (V1 vs. V2)
* **Versão 1 (Baseline):** O modelo aprendeu a classificar apenas pelo valor (`valor <= 1550.0`), ignorando o horário da transação. Em testes de estresse, bloqueou compras legítimas diurnas e aprovou fraudes de baixo valor na madrugada.
* **Versão 2 (Ajuste de Viés):** Após enriquecer o dataset de treino com cenários mistos (compras altas diurnas e compras baixas noturnas), a Árvore de Decisão passou a cruzar **horário + valor**, corrigindo os falsos positivos e falsos negativos no teste de validação.

## 🚀 Como Executar
Clique no selo **Open in Colab** dentro do arquivo `detector_fraudes_ml.ipynb` para executar todas as células diretamente no navegador.
