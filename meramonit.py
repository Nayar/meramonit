#!/usr/bin/python
import json,sys

obj=json.load(sys.stdin)
#print obj

services = obj['monit']['service']
del obj['monit']['service']
print json.dumps(obj)
for service in services:
        obj = {
                "monit": {
                        "service": service
                }
        }
        print json.dumps(obj)
