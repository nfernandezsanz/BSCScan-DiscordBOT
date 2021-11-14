import io
import os
from   configparser import ConfigParser

def read_bots():
    lista = list()
    config = ConfigParser() 
    config.read('config.env') 
    bots = config.sections();
    print ("I have " + str(len(bots)) + " bots")

    for x in bots:
        bot   = dict()
        info = config.options(x)
        if('coin' in info and 'token' in info and 'contract' in info):
            try:
                coin      = str(config.get(x,'coin')).replace('"', "")
                token     = str(config.get(x,'token')).replace('"', "")
                contract  = str(config.get(x,'contract')).replace('"', "")
                info_      = list()
                info_.append(token)
                info_.append(contract)
                bot[coin] = info_
                lista.append(bot)
            except:
                print(str(x) + " has invalid information!")
        else:
            print(str(x) + " has invalid information!")
    return lista

print(read_bots())