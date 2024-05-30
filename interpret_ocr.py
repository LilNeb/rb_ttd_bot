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

def get_status_from_ocr_results(ocr_results_json):
    ocr_results = json.loads(ocr_results_json)
    status_result = {}
    for status, keyword in status_mapping.items():
        status_result[status] = "true" if any(keyword in value.lower() for value in ocr_results.values()) else "false"
    # print(status_result)
    return json.dumps(status_result)

# print(get_status_from_ocr_results(
#     r'''
#     {"Original Image": "Units4\n", "Grayscale Image": "WUnits4\n", "Thresholded Image": "ints\n", "Opening Image": " Girti\n", "Canny Image": "K\n"}
#     '''))

