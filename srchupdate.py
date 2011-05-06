import os
import logging

domain_dir = "/a/mattdeboard.net/"
appdir = domain_dir + "src/yukproj/"
whoosh_dir = appdir + "yuk/whoosh/"

def update():
    logging.basicConfig(filename='/a/mattdeboard.net/src/index.log', 
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S %p')
#    logging.info('Starting index update.')
    status = os.system("cd %s; . bin/activate; cd %s; sudo chown matt:matt %s; "
                       "sudo chown matt:matt %s*; ./manage.py update_index; sud"
                       "o chown www-data:www-data %s; sudo chown www-data:www-d"
                       "ata %s*; sudo /etc/init.d/apache2 force-reload" % 
                       (domain_dir, appdir, whoosh_dir, whoosh_dir, whoosh_dir, 
                        whoosh_dir))
#    logging.info('Index successfully updated.')
    logging.info("Exit status: %s" % status)


if __name__ == '__main__':
    update()

