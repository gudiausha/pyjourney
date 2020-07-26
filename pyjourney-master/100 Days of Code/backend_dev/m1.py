import face_recognition as fr
import json

def m1_service(file1,file2):
    file1 = fr.load_image_file(file1)
    file2 = fr.load_image_file(file2)

    known_encoding = [fr.face_encodings(file1)[0]]
    obama_encoding = fr.face_encodings(file2)[0]

    face_distances = fr.face_distance(known_encoding, obama_encoding)
    face_distances = face_distances.tolist()
    return (face_distances)
    # resp_data = {"match": face_distances} # convert numpy._bool to bool for json.dumps
    # resp_json = json.dumps(resp_data)
    # print(resp_json)
    # return(resp_json)

    # print("The distance between two faces is: ")
    # print (json.dumps(resp_data) )
    # return()


# if __name__ == '__main__':
#     file1='C:/Users/USER/Desktop/python/biden.jpg'
#     file2='C:/Users/USER/Desktop/python/obama.jpg'
#     m1_service(file1,file2)
