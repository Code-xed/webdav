# A Simple WEBDAV-Like Interface.

# How To Run


*clone this repo*

``` bash
cd webdav
pip3 install -U requirements.txt
sudo apt install gunicorn 
gunicorn -b 0.0.0.0:5000 main:app 
```
