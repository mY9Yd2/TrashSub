## About  
TrashSub: auto translate ASS dialogues with DeepL (free) API  
You have to use your own API KEY:  
Create `deepL.txt` file, put your private API KEY there and save it.  
Put your `foo.ass` file in the same dir, rename it to `input.ass`.  
**SLOW**
```bash
# Translate input.ass file
./main.py > output.txt
# Create ASS file from output.txt
./create_ass_file.py > final.ass
```
The script is not too big, you can easily modify to your needs.
