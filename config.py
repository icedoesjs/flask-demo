import yaml
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    

class Config():
    favorite_people = config['favorite_people']