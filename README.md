# Vividarts_studio
 Help Vividarts setup the right environment

About The Project
There are many great README templates available on GitHub; We will use this to document everything that we did in this project. some other resources are: joshseven,

What to note down:

Did you work with anyone, note that
What was the problem you were trying to tackle & how did you go about finding your solution
any challenges you faced and how did you solve them
Collaborations
This is a hand-on cloud engineering project delivered by the azubi africa cloud team in 2023. After 6 months of AWS cloud training and front-end development, we got a chance to work on some realife cloud projects. I was able to work with:

Prince Frimpong @www.linkedin.com/in/frimpong-prince
Lawoe Gayheart Mawuena @
Faith Ashiono
Josphat Too Langat
Rahab Kihuha
Zenat Ahmed Kasili

Project Overview
   Todo and technologies
Key Factors to think about
1. Containerization: 

Implement a solution that allows the seamless deployment of applications across different environments using containerization. This ensures flexibility and consistency, enabling the system to adapt to varying infrastructures.

2. Automated Photo Editing Workflow:

Design an automated workflow for photo editing that enhances the efficiency of the editing tools. This could involve the use of background processes or serverless functions triggered by photo uploads, minimizing manual intervention.

3. Cloud Storage for Accessibility:

Utilize cloud storage solutions, to store and manage photos. This not only ensures easy accessibility but also provides a scalable and durable storage infrastructure.
create 2 S3 buckets.
First Buckets will receive the image when uploaded from the web interface
Second Bucket will resize the image and transform it to a different form
4. User-Friendly Interfaces:
- Drop down the templates and modify the index.html, save it but install python3 and flask in the environment 
- run python3 pip app.py
- Click the URL to link you to the web page
- Search for form in the wylex.js file and edit it, then save
- app.py : import flask,boto3
- Go and create the first s3 bucket you will upload the image, Replace the bucket name, access key and secret key, return render_template("index.html") put index.html in the round brackets
- Go create lambda function, mage = image.convert("L") ,
Focus on creating intuitive and user-friendly interfaces for both photographers and clients. This includes streamlining the photo upload process and providing feedback options.

5. Infrastructure as Code (IaC):

Implement Infrastructure as Code to automate the provisioning and management of infrastructure resources. 

6. Monitoring and Analytics:

Identify bottlenecks, and gather insights for continuous improvement.

7. Continuous Integration/Continuous Deployment (CI/CD):

Implement CI/CD pipelines to automate the testing and deployment of changes, ensuring a rapid and reliable release cycle.
   
   
Getting Started
This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

Installation
Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services.

Clone the repo
git clone https://github.com/lawrencemuema/Vividarts_studio
(back to top)

Contact
Prince Frimpong - @my_twitter - loompesky@yahoo.com

Project Link: https://github.com/your_username/repo_name

(back to top)

References
Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

https://azubi-africa.gitbook.io/vividarts/lets-break-it-down

file:///Users/pfrimpong/Downloads/Uploading%20files%20to%20AWS%20S3%20with%20Flask%20_%20by%20Aniket%20Wattamwar%20_%20AWS%20Pocket%20_%20Medium.html

http://127.0.0.1:5000/upload

Uploading files to AWS S3 with Flask | by Aniket Wattamwar | AWS Pocket | Medium

https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html?refid=3da65280-58c3-4e9f-8d04-5402461fedce
