#!/usr/bin/env python3

import requests

import config

sourceurl = "https://cve.lineageos.org/api/cves"
targeturl = "http://cve.zap.z3ntu.xyz"

mitrelink = 'https://cve.mitre.org/cgi-bin/cvename.cgi?name='

cves = requests.get(sourceurl).json()

headers = {'Apikey': config.apikey}

print(cves)
for key, value in cves.items():
    # cve_id
    # cve_notes
    # -> /addcve
    # cve_id
    # link_url
    # link_desc
    # -> /addlink

    addcveobj = {"cve_id": key, "cve_notes": value['notes']}
    # Fix empty notes
    if addcveobj['cve_notes'] is None:
        print("ERROR! Upstream has empty notes..")
        addcveobj['cve_notes'] = "No notes on cve.lineageos.org"
    elif len(addcveobj['cve_notes']) < 10:
        print("ERROR! Upstream has notes < 10 characters: " + addcveobj['cve_notes'])
        addcveobj['cve_notes'] += " - notes too short on cve.lineageos.org"

    res = requests.post(targeturl + "/addcve", json=addcveobj, headers=headers)

    # Print error
    if res.json().get('error') != "success":
        print("ERROR!")
        print("Request:")
        print(addcveobj)
        print("Response:")
        print(res.json())
        continue
    cve_id = res.json().get('cve_id')

    # /addcve
    for link in value['links']:
        # Skip auto-generated notes (at least for now)
        if link.get('link') == mitrelink + key:
            continue

        addlinkobj = {'cve_id': cve_id, 'link_url': link.get('link'), 'link_desc': link.get('desc')}
        res = requests.post(targeturl + "/addlink", json=addlinkobj, headers=headers)

        # Print error
        if res.json().get('error') != "success":
            print("ERROR!")
            print("Request:")
            print(addlinkobj)
            print("Response:")
            print(res.json())

print("FINISHED!")
