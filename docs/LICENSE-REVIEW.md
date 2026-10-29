# Revisão de licenças

Verificação em 29/10/2026. Escopo: materiais disponíveis e referências primárias abaixo; não houve auditoria de código ausente.

| Componente | Constatação | Tratamento |
| --- | --- | --- |
| FM-1-transporter | Repositório upstream declara MIT; LICENSE identifica copyright de 2026 de kurogedelic | Apenas link; código não copiado |
| jl-uboot-tool | Repositório upstream identifica MIT | Apenas link; código e loaders não copiados |
| MvaveFM1Unbricker | URL/revisão e licença da cópia usada não confirmadas | Excluído |
| Leitor experimental e alterações locais | Arquivos completos e cadeia de autoria indisponíveis | Trechos de código excluídos |
| Pico SDK, TinyUSB, Pico-PIO-USB e demais dependências | Revisões locais e avisos completos não auditados | Não empacotados |
| Firmware FWSC, loaders e dumps | Permissão específica de redistribuição não demonstrada | Não empacotados |

Fontes primárias:

- https://github.com/kurogedelic/FM-1-transporter
- https://github.com/kurogedelic/FM-1-transporter/blob/main/LICENSE
- https://github.com/kagaimiq/jl-uboot-tool

A declaração de licença de um repositório não comprova autorização para todo binário de terceiros usado com ele. Qualquer futura inclusão de código MIT deverá preservar os avisos de copyright e o texto da licença correspondente. A licença atual do upstream não identifica automaticamente a licença de cada versão local antiga.

Esta preparação não aplica MIT ou outra licença global a materiais de autoria ou origem não confirmadas.
