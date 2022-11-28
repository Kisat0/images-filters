import sys
import filters.pipeline as p
import config as c
import logger as log
import configparser as cp
import config as dict
import os
import features.video2img as vid
import features.gif_maker as gif


args = sys.argv


def formatFiltersArray(filtersArg):
    """
    Format string for cli
    :param filtersArg: string who needs format
    :return: string formating
    """
    list = filtersArg.split("|")
    return list

def set_config(inifile):
    """
    take a default parameter from ini file
    :param inifile: file where there are the default parameters
    :return:
    """

    config = cp.ConfigParser()
    config.read(inifile)

    try:
        if config["general"]["input_dir"] != "":
            dict.config_setup["input"] = config["general"]["input_dir"] + "/"
    except:
        pass

    try:
        if config["general"]["output_dir"] != "":
            dict.config_setup["output"] = config["general"]["output_dir"]
    except:
        pass

    try:
        if config["general"]["log_file"] != "":
            dict.config_setup["logfile"] = config["general"]["log_file"]
    except:
        pass

    try:
        if config["filters"]["filter"] != "":
            dict.config_setup["filters"] = config["filters"]["filter"].split("|")
    except:
        pass

    print(dict.config_setup)

def execute():
    """
    execute all function in project
    :return:
    """

    if args[1] == 'imagefilter':

        for i in range(0, len(args)):
            if args[i] == '-i' or args[i] == '-input-dir':
                input_dir = args[i+1]
                c.config_setup["input"] = input_dir + "/"

            elif args[i] == '-o' or args[i] == '-output-dir':
                output_dir = args[i+1]
                c.config_setup["output"] = output_dir + "/"

            elif args[i] == '-h' or args[i] == '--help':
                print("usage: imagefilter\n"
                      "-h,----help \n"
                      "-i,--input-dir <directory>\n"
                      "-o,--output-dir <directory>\n")
                break

            elif args[i] == '--config-file':
                set_config(args[i+1])
                p.pipeline_filter(c.config_setup)
                break

            elif args[i] == '--set-log-file':
                logfile = args[i+1]
                c.config_setup["logfile"] = logfile
                break

            elif args[i] == '--log-file':
                log.dump_log()
                break

            elif args[i] == '--video':
                video = args[i+1]
                path = args[i+2]
                vid.video2img(video,path)

            elif args[i] == '--gif':
                images = args[i+1] + "/"
                output = args[i+2]
                gif.image2gif(images,output)

            elif args[i] == '--filters':
                filters = formatFiltersArray(args[i + 1])
                c.config_setup["filters"] = filters
                p.pipeline_filter(c.config_setup)

            elif args[i] == '--list-filters':
                filtersList = os.listdir('filters')
                filtersList.remove('__init__.py')
                filtersList.remove('pipeline.py')
                print("🪄Liste des filtres disponibles: 🪄")
                for filter in filtersList:
                    print(filter.split('.py')[0])
                break