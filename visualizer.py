import matplotlib.pyplot as plt
import numpy as np
import wave

# Open the WAV file
with wave.open('sound.wav', 'rb') as wav_file:
    # Get the number of frames and the frame rate
    num_frames = wav_file.getnframes()
    frame_rate = wav_file.getframerate()

    # Read the frames as bytes
    frames = wav_file.readframes(num_frames)

    # Convert the bytes to a numpy array
    sound_data = np.frombuffer(frames, dtype=np.int64)

# Create a time array based on the frame rate and number of frames
time = time = np.arange(0, num_frames/float(frame_rate), 1/float(frame_rate)*2)

# Plot the sound wave
plt.plot(time, sound_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()