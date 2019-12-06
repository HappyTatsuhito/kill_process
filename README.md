# Overview  
起動しているターミナル、プロセスを落とすプログラムになります。　　

# Download  
ホームなどにスクリプトのみをダウンロードする場合は　　

`$ wget https://raw.githubusercontent.com/HappyTatsuhito/kill_process/master/kill_process.py`　　

でダウンロードして下さい。　　

# Usage  
`$ python kill_process.py -オプション`　　

`$ ./kill_process.py -オプション`　　

などで実行して下さい。　　
`-a` : 全てのプロセスを停止し、ターミナルも落とします。  
`-r` : 実行中のプロセスを停止し、ターミナルは残します。  

# Caution  
オプションに`-a`を使用した場合、エディタも同時に閉じてしまうので御注意を  