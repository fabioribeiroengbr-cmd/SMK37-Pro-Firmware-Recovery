# Como contribuir / How to contribute

Você pode ajudar mesmo sem ter recuperado o teclado: documente uma observação verificável, uma falha reproduzível ou uma revisão de hardware. Não apresente compilação bem-sucedida como recuperação funcional.

1. Abra uma issue usando o modelo de relato de teste ou de referência técnica.
2. Identifique modelo, revisão de placa, estado inicial, sistema operacional e ferramenta/commit usados.
3. Descreva a operação exata e o resultado observado. Diferencie leitura, escrita em RAM e escrita/apagamento de flash.
4. Anexe apenas logs revisados e fotos sem dados pessoais. Preserve uma cópia privada antes de editar.
5. Para código, indique upstream, commit de origem, licença e alterações. Inclua os avisos exigidos pela licença. Não envie dumps ou firmware proprietário sem autorização.

Não é necessário enviar o arquivo de firmware para informar nome, tamanho, origem e SHA-256. Um hash identifica bytes; não comprova compatibilidade ou permissão de redistribuição.

## Critérios para uma recuperação confirmada

- Revisão de hardware e ferramenta identificadas;
- Procedimento completo reproduzível e resultado da verificação de gravação documentados;
- Inicialização após desligar e ligar novamente;
- Enumeração USB/MIDI e teste de notas, controles e display, registrando o que foi efetivamente testado;
- Limitações e diferenças entre unidades descritas.

Um único relato deve ser identificado como resultado daquela unidade. Só amplie a compatibilidade após evidências em outras unidades/revisões.

## English

Reports of failed attempts are welcome. Include hardware revision, initial symptoms, OS, exact tool commit, operation performed and observed result. Distinguish build success from device recovery and RAM writes from flash writes. Keep original logs private and submit only reviewed extracts. Do not attach proprietary firmware, loaders, full dumps, personal identifiers or credentials. Attribute all contributed code and retain applicable license notices. No blanket license has been selected for this repository; see LICENSE-NOTICE.md.
