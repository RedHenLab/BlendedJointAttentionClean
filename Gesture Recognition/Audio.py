import glob     # Import glob to easily loop over files
import pympi    # Import pympi to work with elan files
import string   # Import string to get the punctuation data

# Define some variables for later use
corpus_root = 'Test_EAF/'
corpus_root1 = 'Result_files'
print glob.glob("Result_files/*")
output_file = '{}/speech_gesture_this.txt'.format(corpus_root1)
ws = list()
time_start = list()
time_end = list()
for file_path in glob.glob('{}/*.eaf'.format(corpus_root)):
    # Initialize the elan file
    eafob = pympi.Elan.Eaf(file_path)
    ort_tier_names = eafob.get_tier_names()
    for ort_tier in ort_tier_names:
        print(ort_tier)
        for annotation in eafob.get_annotation_data_for_tier(ort_tier):
            utterance = annotation[2]
            words = utterance.split()
            for word in words:
                # Remove the possible punctuation
                
                for char in string.punctuation:
                    word = word.replace(char, '')
                # Convert to lowercase
                word = word.lower()
                if(word == 'this'):
                    ws.append(word)
                    time_start.append(annotation[0])
                    time_end.append(annotation[1])
# print(time_start)
with open(output_file, 'w') as output_file:
    # Loop throught the words with their frequencies, we do this sorted because
    # the file will then be more easily searchable
    for i in range(len(ws)):
        # We write the output separated by tabs
        output_file.write('{}\t{}\t{}\n'.format(time_start[i], time_end[i], ws[i]))
        