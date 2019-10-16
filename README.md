# CARD_TX2
This repo will be used to setup the required files, folders and scripts on the TX2s for the CARD project.

1. **tstest.py**
 
   This file is used to collect data and send files needed as input to the Dashboard
      
2. **logs**
   
   This folder is used store the kaldi text output and would be checked by the tstest.py script to count the number of files in it.
         
3. **soundfiles**
   
   This folder is used store the audio recordings and would be checked by the tstest.py script to count the number of files in it.
   
4. **cardscript.py**
   
   This file is used record audio files and run kaldi ASR on them.
   
5. **clear.py**
   
   This file is used to clear files before running.

