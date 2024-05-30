import utils
import json

status_mapping = utils.status_mapping

def check_status(ocr_results, status):
    # print(status_mapping[status])
    # ocr_results = json.loads(ocr_results_json)
    
    # check if status_mapping[status] is contained in any fields of ocr_results
    for key, value in ocr_results.items():
        if status_mapping[status] in value.lower():
            # print(f"Status {status} is TRUE")
            return True
    # print(f"Status {status} is FALSE")
    return False

def get_status_from_ocr_results(ocr_results):
    # If ocr_results is a string, convert it to a dictionary
    if isinstance(ocr_results, str):
        ocr_results = json.loads(ocr_results)

    status_result = {}
    for status in status_mapping.keys():
        status_result[status] = check_status(ocr_results[status], status)
    return status_result



# Test

# ocr_results = {
#     "lobby": {
#         "Original Image": "Wunits4\n",
#         "Grayscale Image": "WUnits4\n",
#         "Thresholded Image": "tinitsd\n",
#         "Opening Image": " Nari\n",
#         "Canny Image": ""
#     },
#     "start_button": {
#         "Original Image": "",
#         "Grayscale Image": "",
#         "Thresholded Image": "",
#         "Opening Image": "",
#         "Canny Image": ""
#     }
# }

# status_result = get_status_from_ocr_results(ocr_results)
# print(status_result)
