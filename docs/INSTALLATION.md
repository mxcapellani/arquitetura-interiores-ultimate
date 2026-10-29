# Instalação e atualização
```bash
git clone https://github.com/mxcapellani/arquitetura-interiores-ultimate.git
cd arquitetura-interiores-ultimate
```
Copiar `.agents/skills/arquitetura-interiores-ultimate/` para `.agents/skills/arquitetura-interiores-ultimate/` do projeto alvo. Se o host não descobrir esse caminho, carregar explicitamente o SKILL.md; não afirmar instalação automática.
Testar: “Me dê duas opções de arquitetura exterior: edifício corporativo e pousada rural”. Conferir dois pares completos PT/EN. Para referência visual, usar host com visão; geração de imagem requer ferramenta adicional.
Atualização: guardar modificações locais, obter a nova versão, consultar CHANGELOG, substituir a pasta e executar as verificações do README. A Skill não exige Python em tempo de uso textual; Python/PyYAML servem à manutenção.
