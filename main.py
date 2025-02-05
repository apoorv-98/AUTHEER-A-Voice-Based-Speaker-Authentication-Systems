import os
import keras
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist, euclidean, cosine
from glob import glob

from model import vggvox_model
from wav_reader import get_fft_spectrum
import constants as c

import speech_recognition as sr
os.chdir(r"/home/aman/Desktop/AUTHEER/vgg")
def build_buckets(max_sec, step_sec, frame_step):
    buckets = {}
    frames_per_sec = int(1/frame_step)
    end_frame = int(max_sec*frames_per_sec)
    step_frame = int(step_sec*frames_per_sec)
    for i in range(0, end_frame+1, step_frame):
        s = i
        s = np.floor((s-7+2)/2) + 1  # conv1
        s = np.floor((s-3)/2) + 1  # mpool1
        s = np.floor((s-5+2)/2) + 1  # conv2
        s = np.floor((s-3)/2) + 1  # mpool2
        s = np.floor((s-3+2)/1) + 1  # conv3
        s = np.floor((s-3+2)/1) + 1  # conv4
        s = np.floor((s-3+2)/1) + 1  # conv5
        s = np.floor((s-3)/2) + 1  # mpool5
        s = np.floor((s-1)/1) + 1  # fc6
        if s > 0:
            buckets[i] = int(s)
    return buckets


def get_embeddings_from_list_file(model, list_file, max_sec):
    buckets = build_buckets(max_sec, c.BUCKET_STEP, c.FRAME_STEP)
    result = pd.read_csv(list_file,delimiter=",",names=['filename','speaker'])
    result['features'] = result['filename'].apply(lambda x: get_fft_spectrum(x, buckets))
    result['embedding'] = result['features'].apply(lambda x: np.squeeze(model.predict(x.reshape(1,*x.shape,1))))   
    return result[['filename','speaker','embedding']]

def get_id_result():
    
    #print("Loading model weights from [{}]....".format(c.WEIGHTS_FILE))
    model = vggvox_model()
    model.load_weights(c.WEIGHTS_FILE)
    #model.summary()
    #print("Processing enroll samples....")
    enroll_result = get_embeddings_from_list_file(model, c.ENROLL_LIST_FILE, c.MAX_SEC)
    enroll_embs = np.array([emb.tolist() for emb in enroll_result['embedding']])
    speakers = enroll_result['speaker']
    #print("Processing test samples....")
    test_result = get_embeddings_from_list_file(model, c.TEST_LIST_FILE, c.MAX_SEC)
    test_embs = np.array([emb.tolist() for emb in test_result['embedding']])
    #print("Comparing test samples against enroll samples....")
    distances = pd.DataFrame(cdist(test_embs, enroll_embs, metric=c.COST_METRIC),columns=speakers)
    dist_t=pd.DataFrame.transpose(distances)
    print(distances)
    dist_t=np.array(dist_t)
    k=np.amin(dist_t,axis=0)
    if(k[0]>.28):
        #by using cosine distance if value if less than 0.2 then it proceed further otherwise halting the proghram.
        print("unauthorized user................")
        return 0
    else:
        en=enroll_result.loc[:,'filename']
        d1=pd.DataFrame(dist_t,columns=['distance'])
        scores = pd.concat([en, d1],axis=1)
        #taking only most similar audio file
        aud=scores[scores['distance']==k[0]]
        k1=list(aud['filename'])
        re= pd.read_csv(c.TEST_LIST_FILE,names=['filename'])
        #taking the single test file.
        k2=list(re['filename'])
        print(k1[0])
        AUDIO_FILE_1 = k1[0]
        AUDIO_FILE_2=k2[0]
        #print(k2[0])
        #now we are going to match the text using google speech to text api.
        # use the audio file as the audio source                                        
        r = sr.Recognizer()
        a=[]
        print("train")
        with sr.AudioFile(AUDIO_FILE_1) as source:
            audio = r.record(source) 
            z=r.recognize_google(audio)
            a=list(z.split(" "))
            l1=len(a)
            print(a)
        b=[]
        s = sr.Recognizer()
        print("test")
        with sr.AudioFile(AUDIO_FILE_2) as source:
            audio = s.record(source) 
            z=s.recognize_google(audio)
            b=list(z.split(" "))
            l2=len(b)
            print(b)
        counter=0
        for i in range(l1):
            if(a[i] in b):
                b.remove(a[i])
                counter+=1
        print(counter)
        if(l1>=l2):
            denom=l1
        else:
            denom=l2
        if(counter/denom>0.8):
            #if usre is authorized by both speaker validation and text matching
            print("true")
            return 1
        else:
            # if text does not match.
            print("false")
            return 2
        keras.backend.clear_session()

if __name__ == '__main__':
    print(get_id_result())
    #keras.backend.clear_session()
    
