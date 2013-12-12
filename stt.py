#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import httplib
import json
import sys

# given an audio input (flac), connects to google speech recognition, returns the text output from google

def speech_to_text(audio):
    url = "www.google.com"
    path = "/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en"
    headers = { "Content-type": "audio/x-flac; rate=44100" };
    params = {"xjerr": "1", "client": "chromium"}
    conn = httplib.HTTPSConnection(url)
    conn.request("POST", path, audio, headers)
    response = conn.getresponse()
    data = response.read()
    jsdata = json.loads(data)
    try:
        # return jsdata["hypotheses"][0]["utterance"]
        return jsdata
    except:
        print "Cat got your tongue?"
        return ""
    #return jsdata

if __name__ == "__main__":
    if len(sys.argv) != 2 or "--help" in sys.argv:
        print "Usage: stt.py <flac-audio-file>"
        sys.exit(-1)
    else:
        with open(sys.argv[1], "r") as f:
            speech = f.read()
        text = speech_to_text(speech)
        print text
