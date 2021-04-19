import configparser

config=configparser.RawConfigParser()
config.read(".\\config\\config.ini")

class readConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseurl")
        return url

    @staticmethod
    def getApplicationUsername():
        user_name = config.get("common info", "username")
        return user_name

    @staticmethod
    def getApplicationPassword():
        password = config.get("common info", "password")
        return password