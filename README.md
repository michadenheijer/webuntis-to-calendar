# Webuntis Calendar

A Python program that exports your webuntis calendar to your google calendar

## How to install

This program runs on Python (3) so you need to install it first. I've made a guide for Windows, macOS and Linux.

### 1: Windows

First you need to download this project as .zip file. You can download this project from this [link](https://github.com/michadenheijer/webuntis-to-calendar/archive/master.zip).

Then you need to install Python 3, you can download that from the [offical Python website](https://www.python.org/downloads/windows/).

Unzip the downloaded project.

Now you need to open the Command Line, and open the folder where you unzipped webuntis-to-calendar.

Now you need to install the requirements using
```batch
pip install -r requirements.txt
```
Continue to step 2.
### 1: macOS

First you need to download this project as .zip file. You can download this project from this [link](https://github.com/michadenheijer/webuntis-to-calendar/archive/master.zip).

Then you need to install Python 3, you can download that from [the offical Python website](https://www.python.org/downloads/mac-osx/).

Unzip the projects and open the folder in the terminal.

Install the requirements using
```bash
sudo pip3 install -r requirements.txt
```

Continue to step 2.

### 1: Linux

Firstly, download this project. To download this program you need to install git. (You can easily install git using ```sudo apt install git -y```).

```bash
git clone https://github.com/michadenheijer/webuntis-to-calendar
```

Go into the directory (example uses the command-line)

```bash
cd webuntis-calendar
```

Firstly test if you have Python 3 installed using:
```bash
python3 --version
```
If it returns something like this then you've got Python installed.
```
Python 3.6.8
```

If you don't have Python installed you can install Python 3 using:

```bash
sudo apt install python3, python3-pip
```

Then install the requirements

```bash
pip3 install -r requirements.txt
```

### 2: Google Calendar API

Now you need to get access to the Google Calendar API.
Go to the [Google Calendar API page](https://developers.google.com/calendar/quickstart/python), and click on the blue **ENABLE THE GOOGLE API** button.
Maybe you need to sign in, finish the prompts, and finally click on the **DOWNLOAD CLIENT CONFIGURATION** button. Place the downloaded file in this projects folder. At this moment you're able to run the program for the first time.

Continue to step 3

## 3: Adding your own data

Now you can run our program. Run it using:
```bash
python3 schedule.py
```

It'll ask for your username and password first. Just fill those in.

Now it asks for your Webuntis server. That is the webadress that you visit to view your Webuntis Schedule. For me it's ```https://kephiso.webuntis.com```.

Now it'll ask for your school, just enter your schoolname.

The last question is about your Webuntis ID. You can find your webuntis id by clicking on the print icon in webuntis, there in the url it should display something like this:

```url
https://{}/WebUntis/api/public/printpreview/timetable?type=5&id=100&date=20190308&formatId=1
```

Your webuntis id is in this example 100.

Now there's a prompt that allows you to login into your Google account. Follow the instructions and you're good to go!

## License

[MIT](LICENSE.md)