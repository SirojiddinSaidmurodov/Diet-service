# Diet-service

## Running
```shell
sudo apt-add-repository ppa:swi-prolog/stable
sudo apt-get update
sudo apt-get install swi-prolog

sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 manage.py start        
```

##Running in docker
```shell
docker-compose up
```