import subprocess
import os
import wave

OUTPUT_DIR = '/mnt/c/Users/zadan/Desktop/'

text_file = open('text.txt', 'r')

def ts():
    return __import__('calendar').timegm(__import__('time').gmtime())

def merge_wav(pname):
    full_path = OUTPUT_DIR + pname
    files_list = os.listdir(full_path)
    combined_wave_file = wave.open(f"{full_path}/combined_files.wav", 'wb')

    params_set = False
    file_index = 1
    for file in files_list:
        wave_file = wave.open(f"{full_path}/{file}", "rb")
        if not params_set:
            # Gets run once in the first iteration
            combined_wave_file.setparams(wave_file.getparams())
            params_set = True
        frames = wave_file.readframes(wave_file.getnframes())
        combined_wave_file.writeframes(frames)
        wave_file.close()
        print(f"file_index: {file_index}")
        file_index += 1
    combined_wave_file.close()


def text_to_speech(project_name):
    full_path = OUTPUT_DIR + project_name

    # Check if the directory exists
    if not os.path.isdir(full_path):
        os.makedirs(full_path)

    # call Mimic 3 command-line interface with the input text
    subprocess.Popen([
        '/home/kw314/.local/bin/mimic3',
        '--output-naming','time',
        '--voice', 'en_UK/apope_low',
        '--output-dir', full_path
    ],
    stdin = text_file
    )

ls_prona = "Alice" + "_" + str(ts()) 
text_to_speech(ls_prona)
merge_wav(ls_prona)

print("Done!")
