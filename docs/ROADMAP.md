# Próximos passos técnicos

| Etapa | Entrega necessária | Situação |
| --- | --- | --- |
| Preservação | Originais privados e hashes | Concluída para os 21 arquivos disponíveis |
| Evidências públicas | Síntese sem dados pessoais e modelos de relato | Disponível |
| Código completo | Árvore do leitor, CMake, patches e identificação de upstream | Ausente neste ambiente |
| Licenças | Conferência arquivo a arquivo e avisos das dependências reais | Depende do código completo |
| Compilação reproduzível | Commits das dependências, comandos e artefatos associados | Ainda não demonstrada |
| Hardware | Revisão da placa, marcações e ligações verificadas | Ainda não documentado no repositório |
| Comunicação | Logs identificando alvo e resultado das operações | Ainda não validada |
| Recuperação | Verificação de gravação e testes após reinicialização | Não comprovada |

A contribuição mais útil agora é recuperar a árvore completa de `SMK37_WL80_Reader` e suas alterações, não publicar um binário sem origem verificável. Não existe comando de build garantido para o leitor experimental enquanto seu CMake completo estiver ausente.

Referências para comparação de código, não instruções de gravação do SMK-37 Pro:

- [FM-1-transporter](https://github.com/kurogedelic/FM-1-transporter)
- [jl-uboot-tool](https://github.com/kagaimiq/jl-uboot-tool)

Os projetos referenciados não são mantidos por este repositório. Compare versões e licenças antes de importar alterações.
