# Instagram Bot - Send Message

Instagram Bot that **automates** your social media interactions to Send Message on Instagram implemented in Python using the Selenium module.

## Installation

**Important:** depending on your system, make sure to use `pip3` and `python3` instead.

```bash
pip install instapy
```

## Usage

You can put in your account details and message string now by setting the values to the designated variables respectively, like so:

```python
insta_username = 'abcd'
insta_password = '1234'
message = 'Some message here'
```

You can also set which users to send the message to, like so:

```python
send_to_list = ['name1', 'name2']
```

Or, you can use [InstaPy](https://pypi.org/project/instapy/0.1.0/#instapy-available-features) features to grab users, like so:

```python
send_to_list = session.pick_mutual_following(username=insta_username, live_match=False, store_locally=True)
```

**Remarks:** if there's error about chromium unable to detect any elements, try increasing the timer value to allow chromium to load longer so that the elements are then being loaded in time, like so:

```python
time.sleep(5.5)
```

### Running Script

Once you have your quickstart script configured you can execute the script with the following commands.

```bash
python quickstart.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
