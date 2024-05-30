import json
import utils

status_mapping = utils.status_mapping

def check_status(ocr_results_json, status):
    # print(status_mapping[status])
    
    ocr_results = json.loads(ocr_results_json)
    # check if status_mapping[status] is contained in any fields of ocr_results_json
    for key, value in ocr_results.items():
        if status_mapping[status] in value.lower():
            print(f"Status {status} is TRUE")
            return True
    print(f"Status {status} is FALSE")
    return False

    
    

check_status(
    r'''
    {"Original Image": "Units4\n", "Grayscale Image": "WUnits4\n", "Thresholded Image": "ints\n", "Opening Image": " Girti\n", "Canny Image": "K\n"}
    '''
    ,"lobby")

