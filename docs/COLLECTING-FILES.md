# Reunir o código para revisão privada

O script `tools/collect_private_sources.py` usa apenas a biblioteca padrão do Python 3. Ele não conversa com o controlador, não grava firmware, não envia arquivos e não altera os originais. Ele precisa ser executado no computador onde o projeto está salvo; a conexão com o GitHub não dá acesso ao seu disco.

## Windows / PowerShell

Baixe o repositório e abra o PowerShell na pasta extraída. Substitua o caminho de exemplo pela pasta real do projeto. Escolha um ZIP novo fora dessa pasta:

```powershell
py -3 .\tools\collect_private_sources.py 'D:\Projetos\SMK37_WL80_Experimental' 'D:\RevisaoPrivada\SMK37-fontes-privadas.zip'
```

O comando acima é um exemplo de caminho, não uma pasta detectada automaticamente. Se o comando `py` não existir e Python estiver instalado como `python`, substitua `py -3` por `python`.

## O que é incluído

Código C/C++, cabeçalhos, Python, PowerShell, CMake, PIO, patches, Markdown e arquivos de licença/configuração selecionados. O ZIP contém um manifesto com tamanho e SHA-256 de cada arquivo copiado. Diretórios de build, Git, ambientes virtuais e arquivos binários não são selecionados. Links simbólicos não são copiados. O ZIP existente nunca é substituído.

## Privacidade e limites

O pacote é **privado**: comentários, nomes de arquivos, configurações e trechos de código ainda podem conter dados pessoais ou ter restrições de licença. A filtragem de algumas credenciais é apenas uma ajuda e não garante anonimização. Não publique esse ZIP automaticamente.

O coletor não é um backup integral: não inclui firmware, UF2, ELF, dumps, fotos ou todos os formatos possíveis. Mantenha separadamente uma cópia integral privada. Para adicionar o conteúdo ao GitHub, revise autoria, licenças e privacidade antes de selecionar cada arquivo.
