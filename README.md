# Network-Intrusion-Detection-System

# Business Problem:

Your task to build network intrusion detection system to detect anamolies and attacks in the network. There are two problems. 

1. Binomial Classification: Activity is normal or attack

2. Multinomial classification: Activity is normal or DOS or PROBE or R2L or U2R

Please note that, currently the dependent variable (target variable) is not definied explicitly. However, you can use attack variable to define the target variable as required.

Steps followed in deploying Machine Learning model using flask to Heroku are-

# 1. Train ML model
We have used Logistic regression, Decision Tree, Random Forest and KNN algorithms however have used Random Forest technique to get the Machine Learning model in predicting the attacks in the network.

# 2. Create a web app using Flask
I have defined the app routes and completing the main.py file, and created a index.html which will serve as the home page, which contains all the field required to run the model.

pocoo_flask_logo_icon_168045

# 3. Commit the code to GitHub
Now create some of the required files for deployement and then commit all the files to GitHub.

Most important thing is to create a Procfile and requirement.txt, which handles the configuration part in order to deploy the model into heroku server. web: gunicorn is the fixed command, after that the first parameter is main.py file i.e the file which will be executed first. Provide the first parameter without the file extension. Second parameter is the flask app name. Requirements consists of all the libraries that has to get installed in heroku environment.

# 4. Connect GitHub to Heroku
Heroku is a multi-language cloud application platform that enables developers to deploy, scale, and manage their applications. Heroku is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market. Heroku gives the direct option to connect with GitHub and deploy the code.

image

# 5. Deploy the model
After successful deployment, app will be created. Check out the web-app: https://network-intrusion-detections.herokuapp.com/
