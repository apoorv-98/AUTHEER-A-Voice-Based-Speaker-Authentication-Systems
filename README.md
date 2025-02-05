# AUTHEER: A Voice-Based Speaker Authentication Systems

This repository is the implementation of the paper "**AUTHEER: A Voice-Based Speaker Authentication Systems**" published in "**International Journal of Advanced Science and Technology**" (**IJAST**). Official source link to the page could be found here:- 
Link - "http://sersc.org/journals/index.php/IJAST/article/view/31493"

## Introduction

Speaker Authentication systems are voice-based user verification and validation systems. They are used to verify if the user is the person he/she claims to be. At their core lies various Deep Learning based algorithms that decide the complete flow of the system. The process starts by system listening to the sound; the speaker produces while speaking. Then the system needs to make sense of the speech and extract words in a particular language. The model used in the project takes the samples of voice for any user as input. These samples are used for model training; the last sample is taken to check for the authenticity of the user. The
model checks for the similarity between voice samples by unique features of the voice and the text converted from the speech. When both the conditions are met, then only the user is truly authenticated for complete system access. The model has also been checked for spoofing possibilities. It was done by using a recorded sample of the user, which could not bypass the model security. So the model provides a great level of security. These systems provide a unique and robust method of authentication that does not require several updates as the voice is an inherent quality of any person. The number of applications is countless ranging from a simple account access system to some complex and sensitive information protection.

## Process for running the above code is quiet simple

### Step1
Initially we need to install all the libraries that are dependent on this project.

### Step2
run the app.py code in cmd or spyder(Anaconda) as python app.py

You will get a local host of the prototype model as localhost:3000

Run the localhost on any browser
