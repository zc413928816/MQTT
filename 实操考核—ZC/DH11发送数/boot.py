
import gc

import os

import network


sta_if = network.WLAN(network.STA_IF)

if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect('ZTE-221', '0123456789@jiaxing')
  #sta_if.connect('zte_331', '123456789')
  #sta_if.connect('nubia', 'yellowlmf1234')
  while not sta_if.isconnected():
    pass
    
    
print('network config:', sta_if.ifconfig())

gc.collect()




