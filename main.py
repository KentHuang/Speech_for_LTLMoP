import stt
import pyaudio_record
import audiotools
import threading

def print_progress (amount_processed, total_amount):
    print "%d%%" % (amount_processed * 100 / total_amount)


def encode(input_file, meta, progress=print_progress):
	audiotools.open(input_file).convert("output.flac", audiotools.FlacAudio)
	return


meta = {    'track_number':1,
            'track_name':u'output',
            'album_name':u'Conatus',
            'artist_name':u'Zola Jesus' }

# record audio
# pyaudio_record.record()
import pyaudio_record


f = open('text_output', 'w')

stopEvent = threading.Event()
RECORDING = False

while True:
		if RECORDING:
			var = raw_input("Press Enter to stop recording")
		else:
			var = raw_input("Press Enter to start or Press 'q' to quit")
		if (var == ''): 
			if not RECORDING:
				#Start new thread with recording function
				recordingThread = threading.Thread(None, pyaudio_record.record, None, [stopEvent], {})
				recordingThread.start()
				RECORDING = True
			else:
				#Set event to stop recording thread
				stopEvent.set()
				recordingThread.join()
				# convert output.wav to flac
				encode('output.wav', meta )
				audio = open("output.flac")
				# connect to google speech recognition
				out = stt.speech_to_text(audio)
				print("You said: " + out)
				f.write(out + "\n")
				RECORDING = False

		if (var == 'q'): break

f.close()
# print out