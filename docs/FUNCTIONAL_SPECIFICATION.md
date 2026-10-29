# Especificação funcional
Entrada: pedido textual e referências opcionais acessíveis. Estado contextual: prompt ativo, atributos fixos, alterações autorizadas, idioma e quantidade. Sem memória externa obrigatória.
Saída padrão: conceito, origem, prompt PT e EN completos. Catálogo retorna IDs e títulos; cópia literal usa biblioteca; adaptação muda apenas o solicitado ou identifica os acréscimos.
Pedido exterior amplo retorna três opções com 04 e 05; pedido de quantidade explícita prevalece. Complementar é devolver prompt completo atualizado. A última alteração explícita substitui somente atributos conflitantes; alvo ambíguo requer esclarecimento curto.
Referências exigem acesso real; dimensões e geometria ocultas não são inferidas como fatos. Erro de entrada essencial gera uma pergunta concreta; omissão estética permite proposta declarada. Ferramentas não disponíveis geram limitação explícita.
Critérios: utilidade imediata, coerência, equivalência bilíngue em adaptações, preservação de requisitos, atribuição e nenhum resultado de ferramenta inventado. Os testes de aceitação especificam evidências para cada contrato.
