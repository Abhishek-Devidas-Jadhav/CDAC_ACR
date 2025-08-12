try:
  import config
except:
  project_home='/home/a/CDAC_ACR'
import numpy as np
from object_detection.utils import label_map_util
import csv

def object_detect(in_path,in_model,count_no):
    selected_image = in_path
    flip_image_horizontally = False
    convert_image_to_grayscale = False

    image_path = IMAGES_FOR_TEST[selected_image]
    image_np = load_image_into_numpy_array(image_path)

    # Flip horizontally
    if(flip_image_horizontally):
      image_np[0] = np.fliplr(image_np[0]).copy()

    # Convert image to grayscale
    if(convert_image_to_grayscale):
      image_np[0] = np.tile(
        np.mean(image_np[0], 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

    # running inference
    results = in_model(image_np)

    # different object detection models have additional results
    # all of them are explained in the documentation
    result = {key:value.numpy() for key,value in results.items()}
    print(result.keys())

    #count object above acc=0.75
    acc=0.75
    #get count of objects detected
    j=0
    for i in (result['detection_classes'][0] + label_id_offset).astype(int):
        if result['detection_scores'][0][j]>=acc:
            count_no[category_index[i]['name']]=count_no[category_index[i]['name']]+1
            #print(f" {category_index[i]['name']} {result['detection_scores'][0][j]}")
        j=j+1

    return count_no

def object_category_index():
    print('Inside object_category_index') #Debugging
    #setting all category to zero
    try:
      PATH_TO_LABELS = f'{config.project_home}/server/.models/research/object_detection/data/mscoco_label_map.pbtxt'
    except:
      PATH_TO_LABELS = f'{project_home}/server/.models/research/object_detection/data/mscoco_label_map.pbtxt'
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
    count_no={}
    j=0
    for i in category_index:
        #print(f" {category_index[i]['name']} {result['detection_scores'][0][j]}")
        count_no[category_index[i]['name']]=0
        j=j+1
    return count_no

    

def write_to_csv(in_path,count_no):
# Writing to CSV file
  with open(in_path, 'w', newline='') as csvfile:
    fieldnames = count_no.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(count_no)
    print(f"Dictionary saved to {csv_file}")
"""
  with open(in_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Key', 'Value'])
          
      # Write data
      for key, value in count_no.items():
          writer.writerow([key, value])
"""
  
    
def send_image_to_database():
    pass

