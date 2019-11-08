# CARD_TX2
This repo will be used to setup the required files, folders and scripts on the TX2s for the CARD project.

1. **send_stats.py**  ~~tstest.py~~  
 
   This file is used to collect data and send files needed as input to the Dashboard. 
   
2. **cardscript.py**
   
   This file is used record audio files and run kaldi ASR on them.
   
3. **clear.py**
   
   This file is used to clear files before running.
      
4. **logs**
   
   This folder is used store the kaldi text output and would be checked by the send_stats.py script to count the number of files decoded.
         
5. **soundfiles16**
   
   This folder is used store the 16KHz bit rate audio recordings and would be checked by the send_stats.py script to count the number of files recorded.
   
6. **soundfiles08**
   
   This folder is used store the 8KHz bit rate audio recordings and would be used by the Kaldi ASR for speech recognition.  
