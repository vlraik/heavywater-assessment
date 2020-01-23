# heavywater-assessment

# How to run it
## To run on localhost, please start with the following command: python application.py. Please make sure that the environment has python 3.5+ and Flask 1.0.2. You can access the webservice locally at localhost:5000. Put the encrypted document/sentence into the input and submit to get the prediction and confidencevalue.

## The webservice is hosted on  AWS elasticbeanstalk and the CI/CD task can be GitHub or GitLab. The reason for choosing AWS elasticbeanstalk is because if provides a lot of benefits in load balancing and scaling the webservice while with the help of other common tools code deployment become 2 clicks away after a proper setup. It can be found at: http://heavywater.j4wammphbu.us-east-2.elasticbeanstalk.com/ 


# Training
### The training documents has a lot of documents and different categories. About 20 million words, but out of which there are 1 million unique words. Therefore, before processing the text documents, we filter out the common words and the most rare words because they would otherwise increase the overfit. We try to further do Exploratory data analysis in the notebook and train the model with 5fold Cross Validation with stratification. Various models like LinearSVC, XGboost, Random Forest, Naive Bayes have been tested but the best results were found with LinearSVC. This model is saved and uploaded to the S3 server, from which it is possible to access the model to the deployed webservice.  

# Testing
### Submit the word onto the webpage and click enter, we get a F-1 score of 87% and it gives the exact confidence and predicted category on submission.

# Further Improvements
### While this was a testing assessment, various types of optimization can be done on cloud management as well as the model itself. For example, if the data is not encrypted, using a NLP pre-trained model like BERT or GPT-2 and retraining the last layers should give a perfect accuracy. Apart from that, we can use AirFlow or make a data workflow management tool which can help us in making a better data pipeline on the cloud. This can be easily ported to AWS stack like Batch or parallel cluster which would help in faster and scalable performance. 
