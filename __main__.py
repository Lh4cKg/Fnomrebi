#!/usr/bin/env python
from phonedb.n_sync import synchronize

# @TODO
# numbers = open('numbers', 'r')

# GSM operator codes

GSM_CODES = ['551', '591', '595', '596', '598', '599', '790', '568', '571', '574', '592', '597', '514', '555', '557',
             '558', '577', '593', '570', '559']

number = 557000558
name = 'Not Found'

synchronize(number=number, name=name)
