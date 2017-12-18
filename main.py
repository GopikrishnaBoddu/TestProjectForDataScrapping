import threading
from queue import Queue

from WebScrapping.spider import  Spider
from WebScrapping.domain import *
from WebScrapping.WebScrapper import *

PROJECT_NAME = "real.de"
HOMEPAGE = "https://www.real.de/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE  = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
