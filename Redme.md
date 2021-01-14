Developed a system that uses the convolutional neural network (CNN) and recognition algorithms, which automatically detects the student when he/she sits in the classroom 
and marks the attendance by recognizing him/her. This system is developed by capturing real-time faces of students sitting in the class. 
Finally, the absentee lists are displayed in the CSV file. This System can be used in Government Schools and Colleges to monitor and validate attendance.
The correctly recognized data gives us accuracy of  approximately 74%.

#Proposed Model

i.Database:  
Videos of 72 students was captured which was then converted to images after various pre-processing like rotating the frames, taking snapshots at each second.
Pre-processing also included cropping the image so that it could train on important features. The images available in the dataset contains the facial images from 0ﹾ to 180ﹾ.

ii.Face Extraction 
The image of classroom is then passed for face extraction. For extracting the face, we have used Harcascade Classifier  
A Haar Cascade is basically a classifier which is used to detect the object for which it has been trained for, from the source. 
The Haar Cascade is trained by superimposing the positive image over a set of negative images. The training is generally done on a server and on various stages.

iii.Storing images and testing: 
The extracted images are stored in a folder as extracted and are passed to the pre-trained model along with two manually added convolutional layers. 
Transfer learning I done from pre-trained model to added layers.VGG-16 Model is a pre-trained model which gives the accuracy of the model. 
Conclusion can be made that CNN model’s classifiers can classify images with more accuracy if transfer learning is used with pre-trained model.

iv.Recognizing faces 
Many algorithms can be used for face detection like using Viola-Jones also know as ada boost algorithm,calculating image gradient in x and y direction and also by consideing 
skin colour but it also detect neck portion.So, HaarCascade Classifier is used. Haar-like features(digital image features used in object recognition) is used by Haar cascade classifier 
for human face detection. There are three formations of Haarlike features. The Algorithm looks for specific haar feature of a face. This detection takes the image and converts it into 
24X24 window and smears each Haar feature to that window pixel by pixel. Initially, the algorithm requires a lot of positive images (images of faces) and negative images 
(images without faces) to train the classifier.

Then, these features are extracted. Features are numerical  values determined from images that are used to distinguish one image from another.Each feature is a single value acquired 
by subtracting the sum of the pixels beneath the white rectangle from the sum of the pixels beneath the black rectangle .
Feature = Σ (pixels in black area) - Σ (pixels in white area)                                  
The faces which were stored in folder is recognized and an array is formed where the students who were recognized is set as 1 and others as 0. 

v.Marking the Attendance 
After the recognition is done by the CNN module based on training set samples,the students which were recognized is marked as present in  CSV file which was automatically generated  using python.
