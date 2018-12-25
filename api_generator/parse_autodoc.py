import yaml

with open("autodoc.yml", "r") as f:
    data = yaml.load(f)
    print(data)


# TODO
# 要らなくなったファイルをどう消す？