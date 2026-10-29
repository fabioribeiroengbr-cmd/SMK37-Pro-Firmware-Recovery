# SMK37-Pro-Firmware-Recovery

Documentação comunitária da investigação de recuperação de um controlador M-VAVE SMK-37 Pro após interrupção de atualização de firmware, registrada em 29/10/2026.

## Estado do projeto

**Experimental. A recuperação funcional do teclado não foi comprovada pelos arquivos disponíveis.** Os registros mostram desenvolvimento, compilação e inspeção de uma variante `smk37_wl80_reader` para RP2040. Este repositório reúne documentação e um coletor local de código para revisão privada. Não contém ferramenta de recuperação executável nem procedimento de gravação validado.

O pacote inicial localizado continha apenas README, inventário e estrutura de pastas. Foram também localizados 20 registros de terminal. Os registros brutos permanecem privados por conterem dados pessoais e trechos de código cuja origem completa não foi verificada.

## Por onde começar

- Está com o teclado sem funcionar? Leia [Comece aqui](docs/START-HERE.md).
- Quer entender a investigação? Consulte [o caso de 29/10/2026](docs/CASE-2026-10-29.md).
- Tem resultados ou referências? Veja [como contribuir](CONTRIBUTING.md) e abra uma issue com um dos modelos.
- Tem o código no computador? Use o [coletor para revisão privada](docs/COLLECTING-FILES.md).
- Quer avançar o projeto? Confira [as etapas e evidências necessárias](docs/ROADMAP.md).

## English

Experimental research into recovery of an M-VAVE SMK-37 Pro after an interrupted firmware update. Available records do **not** demonstrate a working recovery. This repository provides evidence summaries, a diagnostic documentation guide, report templates and a local source collector for private review. It does not provide a validated flashing tool, firmware image or verified SMK-37 Pro wiring diagram. Reports in English are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## Conteúdo

- [Inventário e evidências](docs/INVENTORY.md)
- [Estado técnico](docs/TECHNICAL-STATUS.md)
- [Licenças e atribuições](docs/LICENSE-REVIEW.md)
- [Revisão de privacidade](docs/PRIVACY-REVIEW.md)

## Limites

Não acompanha firmware do fabricante, loader, dumps, executáveis, UF2 ou código de terceiros. A documentação do FM-1 é uma referência de pesquisa e não demonstra compatibilidade de gravação com o SMK-37 Pro. Não use imagens de outro equipamento para recuperar este controlador.

## Contribuições

Relatos úteis devem identificar revisão de hardware, versão da ferramenta e resultado observado. Remova identificadores pessoais antes de compartilhar logs. Não envie firmware ou dumps sem comprovação de permissão de redistribuição.

Projeto independente, sem vínculo com M-VAVE ou JieLi. Licenciamento desta documentação: consultar LICENSE-NOTICE.md.
