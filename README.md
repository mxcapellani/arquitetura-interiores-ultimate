# Arquitetura e Interiores Ultimate

Skill especializada em criar, selecionar, complementar e revisar prompts de arquitetura exterior e design de interiores. Entrega PT-BR e inglês, com direção de materiais, iluminação, câmera e composição.

## O que está incluído
Os **29 prompts bilíngues completos estão no próprio [SKILL.md](.agents/skills/arquitetura-interiores-ultimate/SKILL.md)**, que funciona sem leitura obrigatória de outros arquivos. O PDF anuncia 30, mas não apresenta o item 27. Catálogo exterior: 01–15. Interiores e cenas artísticas: 16–26 e 28–30.

A biblioteca inclui Edifício Corporativo, Pousada Rural, fachadas, residências, lofts, cozinhas, hotel, banheiro, aquarela e low-poly. Preserva textos documentados; não afirma replicar um agente original não testado.

## Experiência de uso
- “Me dê prompts para arquitetura exterior.” → três opções completas PT/EN, incluindo edifício corporativo e pousada rural.
- “Quais temas de interiores você tem?” → catálogo de títulos e IDs.
- “Quero o prompt original 05.” → texto literal PT/EN do PDF.
- “Complemente com piscina e montanhas.” → prompt ativo inteiro atualizado, identificado como adaptação.
- “Só troque a luz para o anoitecer.” → mantém os outros atributos.
- “Melhore meu prompt” ou “Crie uma biblioteca pública contemporânea” → revisão ou criação nova.

As melhorias Ultimate são fluxos novos de complementação, variação, análise de referência e verificação. Sua eficácia comportamental permanece sujeita aos testes descritos no pacote.

## Instalação
Clone o repositório e copie a pasta `.agents/skills/arquitetura-interiores-ultimate` para a mesma estrutura no projeto de destino. O host precisa reconhecer Skills ou carregar explicitamente o SKILL.md como instrução. Descoberta automática depende da plataforma; o repositório não instala plugins nem habilita ferramentas por si só. Veja [instalação](docs/INSTALLATION.md).

## Requisitos e permissões
Modelo de linguagem para uso textual; visão/acesso a arquivos opcionais para referências; ferramenta de imagem opcional e separada para renderizar. Sem chave/API obrigatória. Não solicita credenciais nem executa publicação ou geração externa automaticamente. Sintaxe específica de fornecedor requer verificação de sua documentação.

## Testes
Python 3.10+ e PyYAML são requisitos apenas do desenvolvimento.
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
```
Validador verifica YAML, links, integridade dos 29 pares e estrutura. Não comprova fidelidade visual. [Aceitação](tests/acceptance-tests.md), [matriz](tests/comparison-matrix.md) e [resultados](tests/validation-results.md) distinguem execução local e cenários pendentes. Actions executa as mesmas verificações estruturais.

## Atualização e limitações
Consultar [CHANGELOG](CHANGELOG.md), preservar alterações locais antes de atualizar e repetir testes após qualquer mudança. Não há garantia de geometria ou resolução do gerador; não substitui projeto executivo ou cálculo técnico. Visão depende do host. [Limitações](docs/LIMITATIONS.md).

## Licença e origem
MIT para as contribuições originais. Os prompts do PDF mantêm os direitos de sua origem ImobLabsIA; veja [NOTICE](NOTICE.md) e [atribuição](docs/SOURCE_AND_ATTRIBUTION.md). O PDF não está incluído e sua presença como referência não significa endosso.
