import sys, os

sys.path.append('./')
# Signal processing
SAMPLE_RATE = 16000
PREEMPHASIS_ALPHA = 0.97
FRAME_LEN = 0.025
FRAME_STEP = 0.01
NUM_FFT = 512
BUCKET_STEP = 1
MAX_SEC = 10

# Model
WEIGHTS_FILE = "data\model\weights.h5"
COST_METRIC = "cosine"  # euclidean or cosine
INPUT_SHAPE=(NUM_FFT,None,1)

# IO
print(os.getcwd())
ENROLL_LIST_FILE = os.path.join('cfg','enroll_list.csv')
print(ENROLL_LIST_FILE)
#ENROLL_LIST_FILE = "\cfg\enroll_list.csv"
TEST_LIST_FILE = os.path.join('cfg','test_list.csv')
#TEST_LIST_FILE = "\cfg\test_list.csv"
RESULT_FILE = r"C:\Users\Aman Jaiswal\Desktop\final\vgg\cfg\res\results.csv"
