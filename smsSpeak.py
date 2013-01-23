#!/usr/bin/python
#-*-coding: utf-8-*_

import android

def main():
	droid = android.Android()
	# get last sms
	query = droid.queryContent("content://sms/inbox",
			["body", "address"],
			None,
			None,
			"date DESC LIMIT 1")
	sms = query.result[0]
	# get address
	query = droid.queryContent("content://com.android.contacts/data/phones",
		["display_name"],
		"data1 = '"+sms["address"]+"' or data4 = '"+sms["address"]+"'",
		None,
		"contact_id LIMIT 1")
	name = query.result[0]["display_name"] if len(query.result) else sms["address"]
	# ttsSpeak
	droid.ttsSpeak("Absender " + name + "schreibt: " + sms["body"])
	

if __name__ == "__main__":
	main()
