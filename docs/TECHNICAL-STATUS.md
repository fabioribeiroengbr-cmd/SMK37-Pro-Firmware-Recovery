# Estado técnico observado

Os registros incluem uma compilação de `fm1_transporter.elf`, uma tentativa do projeto experimental interrompida por erro sintático em `transporter_proto.c` e inspeções posteriores do código. A listagem final registra ELF e UF2 do leitor experimental com datas de modificação 29/10/2026 00:32:28 e 00:32:29, respectivamente. Isso demonstra uma listagem de artefatos, não validação de sua execução ou recuperação do teclado.

A configuração efetiva exibida contém `FM1T_HOST_ONLY=1`, `FM1T_BOARD_DEBUGPROBE=0` e `PICO_BOARD=pico`. Não é correto apresentar essa compilação como uma imagem confirmada para Seeed XIAO apenas por o hardware de referência usar RP2040.

Uma descrição no código chama o protocolo de subconjunto somente de leitura, mas os trechos também mostram rotinas de escrita, apagamento e salto. Portanto, a segurança de somente leitura não está demonstrada.

Não foram encontrados nos materiais disponíveis: teste funcional final do teclado, comparação de dump antes/depois, confirmação de gravação verificada ou uma árvore completa de código com revisão identificada. As instruções de gravação e limites de memória do FM-1 não foram transpostos para o SMK-37 Pro.

Para evoluir para uma ferramenta reproduzível será necessário recuperar os arquivos completos do computador original, identificar versões das dependências e confrontar os binários com o código correspondente.
