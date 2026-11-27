# Compilado — yt-dlp, FFmpeg, Deno e compartilhamento VMware

**Gerado em:** 05/11/2026 às 14:03 (UTC−03:00)

> **Nota de formatação:** este Markdown utiliza HTML/CSS para cores. A exibição depende do visualizador.

## Sumário

1. [Diagnóstico inicial do erro HTTP 400](#sec-1)
2. [Atualização e localização do yt-dlp](#sec-2)
3. [Runtime JavaScript e Deno](#sec-3)
4. [FFmpeg e seleção de trechos](#sec-4)
5. [Travamento do vídeo e solução encontrada](#sec-5)
6. [Resolução e formatos de download](#sec-6)
7. [Combinação de áudio e vídeo](#sec-7)
8. [Pasta de destino e nome do arquivo](#sec-8)
9. [Diretório /mnt e montagem de arquivos](#sec-9)
10. [VMware HGFS e compartilhamento com o Windows](#sec-10)
11. [Resumo dos comandos principais](#sec-11)

<a id="sec-1"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">1. Diagnóstico inicial do erro HTTP 400</h2>

O vídeo do YouTube (ID ysILFciOLh8) era identificado, mas o yt-dlp 2024.04.09 retornava “HTTP Error 400: Bad Request” e “Only images are available for download”. O problema aparecia até na listagem de formatos, antes do corte.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -F "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>

A opção -F lista os formatos oferecidos. Para obter informações detalhadas de diagnóstico, usa-se -v.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -v -F "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>


<a id="sec-2"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">2. Atualização e localização do yt-dlp</h2>

A versão antiga era 2024.04.09 e o executável estava em /usr/bin/yt-dlp. Uma nova versão, 2026.10.26, foi instalada em /usr/local/bin/yt-dlp. O sistema pode manter ambas as instalações.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
which yt-dlp
yt-dlp --version
type -a yt-dlp
/usr/local/bin/yt-dlp --version
ls -lh /usr/local/bin/yt-dlp
```

</div>

A instalação separada do executável oficial foi feita com os comandos abaixo. O download executável deve ser obtido apenas da fonte oficial.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

</div>

Se o shell ainda usar um caminho antigo em cache, limpe a tabela de comandos e confira a versão.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
hash -r
yt-dlp --version
```

</div>


<a id="sec-3"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">3. Runtime JavaScript e Deno</h2>

A versão atualizada avisou que nenhum runtime JavaScript compatível estava disponível. Um runtime executa código JavaScript fora do navegador. O yt-dlp o utiliza para resolver desafios do YouTube e recuperar determinados formatos.

O Deno foi instalado; o log posterior confirmou “JS runtimes: deno-2.9.8” e “Solving JS challenges using deno”.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
curl -fsSL https://deno.land/install.sh | sh
deno --version
```

</div>

A instalação acima executa um script remoto; confirme que confia na fonte. Documentação: https://github.com/yt-dlp/yt-dlp/wiki/EJS


<a id="sec-4"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">4. FFmpeg e seleção de trechos</h2>

O FFmpeg 6.1.1 e o ffprobe 6.1.1 estavam disponíveis. A sintaxe de --download-sections exige um asterisco antes de intervalos de tempo. Sem o asterisco, “00:02-04:40” é interpretado como padrão de nome de capítulo, levando à mensagem “Cannot match chapters”.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
ffmpeg -version
yt-dlp --download-sections "*00:02-04:40" "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>

O intervalo de 00:02 até 04:40 corresponde a aproximadamente 4 minutos e 38 segundos. --force-keyframes-at-cuts recodifica para buscar cortes mais precisos, podendo consumir mais tempo.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp --download-sections "*00:02-04:40" --force-keyframes-at-cuts "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>


<a id="sec-5"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">5. Travamento do vídeo e solução encontrada</h2>

O primeiro arquivo parava de reproduzir após alguns segundos. Ao remover apenas a opção --force-keyframes-at-cuts, sem desinstalar o FFmpeg, o vídeo passou a reproduzir normalmente. Isso aponta para um problema associado à recodificação naquela tentativa, mas não comprova uma falha geral do FFmpeg.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp --download-sections "*00:02-04:40" "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>

Para investigar arquivos defeituosos, podem ser usados estes testes de decodificação e duração:

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
ffmpeg -v error -i "nome_do_video.mp4" -f null -
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "nome_do_video.mp4"
```

</div>


<a id="sec-6"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">6. Resolução e formatos de download</h2>

A opção -f escolhe formatos. O seletor abaixo limita a resolução máxima a 1080p; não garante exatamente 1080p. Sem -f, o yt-dlp seleciona automaticamente formatos segundo seus critérios de qualidade e disponibilidade.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -f "bv*[height<=1080]+ba/b" "URL"
yt-dlp -F "URL"
```

</div>

O comando abaixo mostra a seleção prevista sem baixar o vídeo:

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp --simulate --print "%(format_id)s | %(resolution)s | %(ext)s" "URL"
```

</div>


<a id="sec-7"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">7. Combinação de áudio e vídeo</h2>

Na seleção -f, o operador + combina formatos: por exemplo, um fluxo somente de vídeo e outro somente de áudio. O FFmpeg normalmente os reúne (muxing) em um arquivo final, sem recodificação. Os IDs abaixo são exemplos e devem existir na lista do vídeo.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -f "137+140" "URL"
yt-dlp -f "137+140" -k "URL"
```

</div>

A opção -k mantém os arquivos intermediários. Já / indica alternativa: se a primeira combinação não estiver disponível, tenta-se a seguinte.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -f "137+140/136+140" "URL"
```

</div>


<a id="sec-8"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">8. Pasta de destino e nome do arquivo</h2>

-P define o diretório de destino; -o define o modelo de nome. %(ext)s é substituído pela extensão real. Sem essas opções, o download geralmente fica no diretório de trabalho atual.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
pwd
mkdir -p ~/Vídeos
yt-dlp -P ~/Vídeos -o "Trecho do video.%(ext)s" "URL"
```

</div>

Exemplo reunindo formatos, corte e pasta de saída:

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp -f "137+140" --download-sections "*00:02-04:40" -P ~/Vídeos -o "Trecho do video.%(ext)s" "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>


<a id="sec-9"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">9. Diretório /mnt e montagem de arquivos</h2>

/mnt é um diretório convencional para pontos de montagem. Montar significa tornar um sistema de arquivos acessível em um diretório. /media costuma ser usado para mídias removíveis, enquanto /home contém arquivos pessoais.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
ls -l /mnt
findmnt
findmnt /mnt/hgfs
```

</div>

Criar uma pasta dentro de /mnt não monta automaticamente nenhum dispositivo.


<a id="sec-10"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">10. VMware HGFS e compartilhamento com o Windows</h2>

HGFS significa Host-Guest File System: permite acessar, no Linux convidado, pastas que o VMware compartilha a partir do sistema hospedeiro. O comando a seguir monta os compartilhamentos disponibilizados pelo VMware em /mnt/hgfs.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```

</div>

sudo executa como administrador; vmhgfs-fuse é o montador; .host:/ é a origem; /mnt/hgfs é o ponto de montagem; -o allow_other permite acesso por outros usuários conforme permissões. O diretório deve existir e o compartilhamento precisa estar configurado no VMware.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
ls /mnt/hgfs/
findmnt /mnt/hgfs
yt-dlp -P "/mnt/hgfs/Compartilhada" "URL"
sudo umount /mnt/hgfs
```

</div>

A montagem não copia arquivos: ela dá acesso à pasta compartilhada. Para gravar nela, o compartilhamento precisa permitir escrita.


<a id="sec-11"></a>
<h2 style="color:#e77d7d; font-size:1.65em;">11. Resumo dos comandos principais</h2>

Sequência recomendada após a correção do ambiente: verificar a versão, consultar os formatos e baixar um trecho sem forçar recodificação.

<div style="background:#143b65; color:#ffe36a; border-radius:8px; padding:12px 16px;">

```bash
yt-dlp --version
deno --version
yt-dlp -F "https://www.youtube.com/watch?v=ysILFciOLh8"
yt-dlp --download-sections "*00:02-04:40" -P ~/Vídeos "https://www.youtube.com/watch?v=ysILFciOLh8"
```

</div>

As instruções documentam os testes e resultados relatados na conversa. URLs, caminhos e IDs de formatos devem ser ajustados conforme o vídeo e o ambiente.
