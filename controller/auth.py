#!/usr/bin/env python
#-*- coding: utf-8 -*-

import hashlib

import packet
import util

#def before(args, data):
#    if data['auth'] == False:
#        return False

def login(args, data):
    psk = data['pkt'].get('psk')

    if psk == hashlib.md5(args['defaults']['psk']).hexdigest():
        print "Auth %s From %s" % (util.green("Success"), str(data['addr']))
        data['sock'].sendall(packet.Packet({}, 'OK').tostr())
        return
    print "Auth %s From %s (psk: %s)" % (util.red("Failed"), str(data['addr']), str(psk))
    data['sock'].sendall(packet.Packet({}, 'REJECT').tostr())
