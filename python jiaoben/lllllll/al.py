import yaml
with  open(file='a.yaml',mode='r',encoding='utf-8')  as fb:
    data = yaml.load(fb,Loader=yaml.FullLoader)
    print(data)