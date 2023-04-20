# pdfView
A simple tool for websites to link to a page containing a PDF,  viewable for their users.


## How Can I Use pdfView?
There are two ways of using pdfView for your own purposes. The first and recommended way by cloning then building a 
Docker image that can be used to create containers on cloud computing tools such as AWS's EC2 or Azure VMs. Otherwise, 
you can fork this repository to make necessary modifications for your use case.

In both cases, you'll need to make some simple modifications to this repository to fit your use case, as well as to 
configure pdfView for production. 

To use pdfView, you'll need some sort of cloud computing solution prepared such as an AWS EC2 instance, or an Azure VM.
If you are going to build and deploy with Docker, clone this repository onto your system. If you are going to manually deploy, 
fork this repository instead.

### Configuration
1. Navigate to the `pdfView/server` directory and run the following commands to create an admin user. You will use this in production to control your site.
```bash
pip install -r requirements.txt 
django-admin createsuperuser
```
2. Create a `.env` file in `pdfView/server/` to hold important, and private values (your `.env` file should not be released publicly). 
3. Run the following commands to create a `SECRET_KEY`, which is necessary for Django.
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Copy the result and place it into `pdfView/server/.env`.
4. In your `.env` file, write `ALLOWED_HOSTS={your host address}`. 
5. Navigate to `pdfView/client` directory and place all PDF files that you wish to be displayed in `/public`.

### Building with Docker
If you are building with Docker, finish up with the following steps.
1. Navigate back to the project root `pdfView` and run the following command to build the Docker image.
```bash
docker compose build
```
This will build an image that can be used to easily create containers that will run pdfView on cloud computing solutions. You can choose whichever method you wish to easily deploy to your cloud computing solution of choice. Here are some resources.
Once the container is running on your cloud computing solution, pdfView is deployed! The last step is production configuration.
### Building manually
If you are building manually, you will have to access your cloud computing solution (such as with SSH for AWS EC2) and 
then clone your repository (to gain the ability to do this is why you forked this repository!) and execute the following steps internally.
1. Navigate to `pdfView/server` and run the following command to install dependencies then start the server.
```bash
pip install -r requirements.txt 
python3 manage.py runserver
```
You should see some text indicating that the server started successfully.
2. Next, navigate to `pdfView/client` to install client dependencies and start the client server.
```bash
npm install
npm start
```
If you see more success text, pdfView is now deployed!
### Production Configuration

Once pdfView has been deployed, set up by entering into the admin site and adding information for each of your PDFs.