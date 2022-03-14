# MSAI_495_project
In the following repo you can find a Cycle Gan that our team has developed during the Winter Semester of our Deep Learning MSAI 495 course. The goal of this project is to develop a model capable of aging and deaging a person’s face based on an image of themselves. Our approach was to develop an Age-Conditional Generative Adversarial Network (GAN), meant to preserve the person’s identity while generating synthetic images which make them appear older or younger. We have used the [Cross-Age Celebrity Dataset](https://bcsiriuschen.github.io/CARC/) in order to complete this project.

To identify the best archichture suitable for generating synthetic images, we constructed, developed and tested many different classification models at first. The final code developed for the classification proccess is presented in the [folder](https://github.com/AleksandrSim/MSA_495_project/tree/main/classification).


Once we have identified the architechture, we have created a Cycle Gan. The code for the Cycle Gan model and training can be found here [here](https://github.com/AleksandrSim/MSA_495_project/tree/main/gan_modeling)


After 5 epochs of training we have achieved the following results:


**old to young**


![old original](https://github.com/AleksandrSim/MSA_495_project/blob/main/files/original_old.png) ![old original](https://github.com/AleksandrSim/MSA_495_project/blob/main/files/young_generated.png)



**young to old**




![young original](https://github.com/AleksandrSim/MSA_495_project/blob/main/files/unnamed%20(1).png) ![old original](https://github.com/AleksandrSim/MSA_495_project/blob/main/files/unnamed%20(2).png)



