import os
import sys
import logging

domain_dir = "/a/mattdeboard.net/"
appdir = domain_dir + "src/yukproj/"
whoosh_dir = appdir + "yuk/whoosh/"

def update():
    logging.basicConfig(filename='/a/mattdeboard.net/src/index.log', 
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Starting index update.')
    try:
        status = os.system("cd %s; . bin/activate; cd %s; sudo chown matt:matt %s; "
                           "sudo chown matt:matt %s*; ./manage.py update_index; sud"
                           "o chown www-data:www-data %s; sudo chown www-data:www-d"
                           "ata %s*; sudo /etc/init.d/apache2 force-reload" % 
                           (domain_dir, appdir, whoosh_dir, whoosh_dir, whoosh_dir, 
                            whoosh_dir))
        if status == 0:
            logging.info('Index successfully updated.')
        else:
            logging.error("Index update failed. Please consult UNIX exit status val"
                          "ues for more information.")
            logging.error("Exit status: %s" % status)
    except:
        logging.error("Exception received:", sys.exc_info()[0]


if __name__ == '__main__':
    update()
