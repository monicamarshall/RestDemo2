# RestDemo2
RestDemo2 is the second version of RestDemo.  RestDemo manages "snippets" ( code snippets ).  The table snippets resides in the restdemo schema.  Snippet attributes are:

id, 
created, 
title, 
code, 
linenos, 
language, 
style, 
highlighted, 
owner_id


RestDemo has one restful resource "Snippet". Snippets can be created, updated, deleted, listed. Unauthenticated users can only read snippets. Any authenticated user can read any snippet. But an authenticated user can only update and delete his own snippets. Snippets are saved in the snippets table in the restdemo schema. RestDemo relies on a postgres database. Path to list snippets is http://www.restdemo.com:8002/snippets Path to list snippet with id = 1 is http://www.restdemo.com:8002/snippets/1.  The port number can be dynamically set in the supervisor configuration file.  The allowed hosts are set in settings.py for the ALLOWED_HOSTS property.


Steps to build the project:

1. Install postgres 12.2
2. Install nginx 1.16

Instructions for installing and configuring postgres, nginx, supervisor, gunicorn are located in the project folders

3. Install python 3.6.3
4. Install all dependent libraries with pip install. All libraries are listed in requirements.txt except for Supervisor, which is installed system wide with yum install.

Supervisor is a graphical tool that allows to start/stop/refresh the RestDemo application and to view logs using a graphical interface instead of command line.

5. Run the sql statements to configure postgres ( Create roles, users, privilegies, schema ) in setuprestdemo.sql, included in the project folder.

6. run the command: python manage.py migrate to build the database.
7. run the command: python manage.py runserver 
8. To run the unit tests change directory to the project RestDemo directory where manage.py is located and then run the command 'python manage.py test --settings=RestDemo.settings --keepdb'.  The command and output to expect are captured in the 'UnitTestingCommandAndOutput' document.
9. To run the BDD test first change directory to the "features" directory and then run the command behave.  If you want to see print statements to appear on the console run the "behave" command with the --no-capture option, like this "behave --no-capture".  The command and output of the behavior tests are captured in the 'BDD_CommandAndOutput.txt' document.
10. To run SoapUI snippets test scenario, install latest version of SoapUI, import the project, run the test steps.
11. There is an option to run HTTPIE tests on the command line.  HTTPIE requires the tool to be installed.  HTTPIE is a much richer tool than the CURL command line utility with colorful visualization of Restful HTTP invocations and responses.  Some sample commands to test the RestDemo restful API are captured in the 'Httpie_samplesReqRsp' document.
12. The MQ app makes MQ services availabl.  MQ services include Sending to a Queue, Sending to a Topic, Receiving from a Queue, Receiving from a Topic.  

13.  Install the MQ broker by extracting the zip file or the tar ball downloaded from the ActiveMQ site for windows or Linux. Open the mq console at:  http://127.0.0.1:8161/admin/, enter the default admin credentials:  admin/admin and create one topic called restdemo_topic and one queue called restdemo_queue.  These are administered objects that must be created before subscribing and sending messages to either one.

14. Install stomp.py in the restdemo virtual environment with the command 'pip install stomp.py'.

15. Make sure the Stomp connector is configured in the ActiveMQ config file.  Instructions for installing and configuring MQ are in the MQ folder.

16. Run the tests in the mq/test folder with the command '(restdemo) C:\data\pythonworkspace2\RestDemo2\RestDemo>python manage.py test --settings=RestDemo.settings --keepdb.  This is the test setup:  2 receivers are setup for restdemo_queue.  2 receivers are setup for restdemo_topic.  The queue sender sends one message to the restdemo_queue.  The topic sender sends 1 message to the restdemo_topic.  Only one of the 2 queue receivers receive the message.  Both topic receivers receive a copy of the message.  
This is the output of the tests:

Using existing test database for alias 'default'...
System check identified no issues (0 silenced).
test_subscribe_send_Queue()
received a message on queue"This is a message sent to restdemo_queue in test case"
0
1
.disconnected
disconnected
test_subscribe_send_Topic()
received a message on topic "This is a message sent to restdemo_topic from test case"
received a message on topic "This is a message sent to restdemo_topic from test case"
0
0
1
1
.disconnected
disconnected

OK
Preserving test database for alias 'default'...

17.  Access the mq web application at:  http://localhost:8000/mq/.  At this link an overview of existing mq channels are listed.  Restdemo_queue and Restdemo_topic are listed.  Select one of the channels and send a text message to it. http://localhost:8000/mq/1/ this restful url will access all messages posted at mq channel with id 1.  At this page you have the option of sending a text message to the channel by entering the message in the input field and clicking on the send button.  To view all messages sent return to the mq link and view all messages enqueued.
