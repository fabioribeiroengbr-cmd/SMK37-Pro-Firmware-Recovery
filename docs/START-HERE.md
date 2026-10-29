# Comece aqui: diagnóstico e preservação

Este guia organiza informações sem mandar gravar firmware. Não existe, neste repositório, um procedimento de recuperação validado para o SMK-37 Pro.

## 1. Registre o estado inicial

Anote modelo exato e versão de firmware anterior, se conhecida. Fotografe display e LEDs e registre a etapa em que a atualização foi interrompida. Não atribua automaticamente um sintoma a bootloader, flash ou alimentação: o mesmo sintoma pode ter várias causas.

## 2. Registre o reconhecimento USB

No Windows, observe o Gerenciador de Dispositivos ao conectar e desconectar o controlador. Anote nome apresentado, código de erro e IDs de hardware quando disponíveis. Ao compartilhar, remova número de série e caminho de instância que identifique a unidade.

Registre cabo, porta e alimentação usados. Se fizer comparação com outro cabo/porta compatível, altere uma variável por vez. A ausência de enumeração sozinha não identifica qual componente falhou.

## 3. Preserve os arquivos existentes

Copie para uma pasta privada o projeto original, configurações, registros e firmware obtido legitimamente. Não edite nem substitua essa cópia. Registre tamanho e SHA-256 dos arquivos relevantes. Não publique firmware, loader ou dump apenas por ele estar disponível para download.

O [coletor local](COLLECTING-FILES.md) reúne uma seleção de código e configuração para revisão privada. Ele não é uma ferramenta de recuperação.

## 4. Documente o hardware sem presumir equivalência

Se a placa já estiver acessível, fotos legíveis das marcações e pontos utilizados podem permitir comparação de revisões. Não abra o equipamento só para preencher um relato. Não adote a pinagem ou os limites de flash do FM-1 como instruções para o SMK-37 Pro.

## 5. Compartilhe um relato útil

Use o modelo de issue. Inclua o que foi tentado, em que ordem e o resultado, inclusive quando nada mudou. Diga explicitamente se não houve escrita, se houve gravação e se existe backup verificado. Consulte [os próximos passos](ROADMAP.md) antes de propor uma imagem de recuperação.
