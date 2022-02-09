import json
import moviepy.editor as moviepy

def names_to_list(name, name_arr):
    """Collects the classnames and number of each object and saves to a list.

    Parameters:
        name (str): the class name of the object
        name_arr (arr): the array containing 
    """
    if len(name_arr) == 0:
        name_arr.append([name, 1])
    else:
        for i in range(len(name_arr)):
            if name_arr[i][0] == name:
                name_arr[i][1] += 1
            elif (i == (len(name_arr)-1)):
                name_arr.append([name, 1])

def return_name_list(name_arr):
    return name_arr

def names_list_to_json(name_arr):
    """
    Saves the list of objects in a json file (to be displayed on a webpage)

    Parameters:
        name_arr (arr): the array containing the objects (and numbers)
    
    Output:
        creates a data.json file which can be accessed using javascript
    """
    # First, convert the list into a dictionary:
    data = {}
    for item in name_arr:
        data[item[0]] = item[1]
    # Then, create a json file with the data:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def convert_to_mp4(video):
    """
    Converts the video file to mp4 to be read by various packages

    Parameters:
        video (arr): file directory link to video (should be data/video/video_name)
    """
    clip = moviepy.VideoFileClip(video)
    clip.write_videofile("data/video/clip.mp4")
