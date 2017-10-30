#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

cli = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
cli.connect('/run/bt-server.sock')

while 1:
	buf = cli.recv(1024)
	if buf == '':
		break
	print(buf)
cli.close()

