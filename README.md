# Webuntis Calendar

A python program that exports your webuntis calendar to your google calendar

## How to install

There're multiple ways to install this program, it's advised to use the Docker method, because that's easier.

### Docker

First you need to install Docker, every OS has a slightly different installation method, so here are some basic instructions for some of them.

#### Windows

Sadly my program cannot run natively on Windows, you can install Ubuntu from the Windows Store and run the program from there.

#### MacOS

Follow the instructions from the [Docker Desktop for Mac installation page](https://docs.docker.com/docker-for-mac/install/).

#### Raspberry Pi

```bash
curl -sSL https://get.docker.com | sh
```

#### Ubuntu

```bash
sudo apt install docker.io
```

### Python (advanced)

Firstly, download this project

``` python
git clone https://github.com/michadenheijer/webuntis-to-calendar
```

Go into the directory (example uses the command-line)

```bash
cd webuntis-calendar
```

Then install the requirements and create your own config

```bash
sudo apt install python3, python3-pip
pip3 install -r requirements
cp config.example.json config.json
```

Edit your config with a text editor (notepad or something), it should look something like this

```json
{
    "username": "your webuntis username",
    "password": "your webuntis password",
    "server": "the webuntis server",
    "school": "your school",
    "webuntis_id": 1,
    "calendar_id": "primary"
}
```

You can find your webuntis id by clicking on the print icon in webuntis, there in the url it should display something like this:

```url
https://{}/WebUntis/api/public/printpreview/timetable?type=5&id=100&date=20190308&formatId=1
```

Your webuntis id is in this example 100.

Now you need to get access to the Google Calendar API.
Go to the [Google Calendar API page](https://developers.google.com/calendar/quickstart/python), and click on the blue ENABLE THE GOOGLE API button.
Maybe you need to sign in, finish the prompts, and finally click on the DOWNLOAD CLIENT CONFIGURAION button. Place the downloaded file in this projects folder. At this moment you're able to run the program for the first time.

```bash
python3 schedule.py
```

Then there'll be a prompt that allows you to login, login and it should work!
