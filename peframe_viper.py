#!/usr/bin/python3

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
