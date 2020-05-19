
import time

def sleep(n_secs):
    time.sleep(n_secs)

def get_timestamp():
    return str(int(time.time()*1000))

def print_parameter(doc_id):
    print("the paramter is: {}".format(doc_id))