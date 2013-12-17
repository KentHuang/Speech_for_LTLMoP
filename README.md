Speech_for_LTLMoP
=================
Google Voice Search is a modified version of this:
http://www.athoughtabroad.com/2013/05/22/using-google-s-speech-recognition-web-service-with-python

The script used to record an audio file can be found here:
http://people.csail.mit.edu/hubert/pyaudio/

Before running the program, you will need to install pyaudio, which can be found in the link above, and python audiotools, which can be found here: http://audiotools.sourceforge.net/install.html

Run the program by calling 'python main.py' in a terminal.
The program first asks the user to press 'Enter' to start recording. 
After the recording starts, the user can then speak into a microphone to record.
The user can then press 'q' to stop the recording.
The recorded audio file is first saved as 'output.wav'. 
It is then converted to FLAC format, 'output.flac', and transcribed through Google Voice Search.
The text output will then be displayed.
If an error occurred in the process, the message 'Cat got your tongue?' will appear.
The user can then press 'Enter' to start the process again.
