## Text to speech (TTS) for 全职高手 novel

1. Extract novel content from [here](http://quanzhigaoshou.booksrc.net/)
```shell
python parhttp.py <start> <end>
``` 

2. Produce mp3 from extracted text using [gTTS](https://github.com/pndurette/gTTS)
```shell
python speakchinese.py <textfile containing list of chapters> 
python speakchinese.py <specific chapter>
```
