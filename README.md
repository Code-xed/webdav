# A Simple WEBDAV-Like Interface.

# How To Run


## Update
```bash
sudo apt update && sudo apt upgrade
```
## Gunicorn
```bash
sudo apt install gunicorn
```

## Clone The Repository
```bash
git clone https://github.com/Code-xed/webdav.git
```

``` bash
cd webdav
pip3 install -r requirements.txt
sudo apt install gunicorn 
gunicorn -b 0.0.0.0:5000 main:app 
```
