import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = ''
chdir = ''  
# backlog = 500              # 监听队列
timeout = 60
# worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = ""
errorlog = ""
