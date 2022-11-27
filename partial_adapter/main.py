import json

from bs4 import BeautifulSoup

from partial_adapter.experiment import Experiment
from partial_adapter.config_acess import XMLConfigAdpter


def main(file_name) -> None:
    extention = file_name.split(".")[-1]
    if extention=="json":
        with open(file_name, encoding="utf8") as file:
            adapter = json.load(file) # dict object already has get method
    elif extention=="xml":
        with open(file_name, encoding="utf8") as file:
            config = file.read()
        bs = BeautifulSoup(config, "xml")
        adapter = XMLConfigAdpter(bs=bs)
    
    experiment = Experiment(config=adapter)
    experiment.run()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
                    prog = 'Train ML model experiment',
                    description = 'train ML model given the config file'
            )
    parser.add_argument('-f', '--file',type=str, default="config.json",
                    help='the config name file')
    args = parser.parse_args()
    main(file_name=args.file)