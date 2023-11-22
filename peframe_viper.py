#!/usr/bin/python3

import viper
from viper.common.out import bold
from viper.common.abstracts import Module
from viper.common.utils import get_type, get_md5
from viper.core.database import Database
from viper.core.storage import get_sample_path
from viper.core.session import __sessions__

import peframe.peframe as pef
class Peframe(Module):
    cmd = 'peframe'
    description = 'Extract information from PE with peframe'
    authors = ['twpzero']
    categories = ["windows"]

    def __init__(self):
        super(Peframe, self).__init__()
        
    def run(self):
        if not __sessions__.is_set():
            # No open session.
            return
      self.log('info','peframe starts now (can take a while)')
      fileinfo = pef.analyse(__sessions__.current.file.path)
      self.log('item',"{}".format(fileinfo)
