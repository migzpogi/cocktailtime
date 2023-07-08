import configparser


class InitProperties:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.__load_config()

    def __load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)

        return config


def from_init():
    return "From init"