# Intro

## What is this workshop?

This workshop is a hands-on guide to making a bot in Discord -- Discord bots have been popular projects for some time now, with no signs of slowing -- a popular bot listing website, [top.gg](https://top.gg) has Discord bots in as many as **one million servers**! In this workshop, we'll make a Discord bot that can act as a simple calculator in Python, a programming language commonly regarded as being simple enough to be approachable by beginners.

# Setup

Getting a Discord bot up and running requires a couple steps; these include getting Python set up and installing required packages, registering a bot with Discord, and having a workspace to test your bot in. For most simple bots, all you'll need on Python's end is a Python version greater than around 3.6 and the `discord.py` library. We'll also use a package called `python-dotenv` to manage some sensitive information.

## Getting Python set up

Some of you will probably already have a Python installation ready to go on your computer -- if that's the case, all you'll need to do is install discord.py: just open a command prompt and enter `python -m pip install discord.py python-dotenv`.

If you don't have Python set up on your computer, you can follow along on the online code editing website [repl.it](https://repl.it): make an account or sign in with Google, GitHub, etc. and create a new Python repl. Enter the __Extensions__ menu from the left-hand tool, and you should be able to search for and install both `discord.py` and `python-dotenv`.

## Getting Discord set up

If you don't have a Discord account, make one now; head to the [Discord website](https://discord.com) and get that set up.

Once you have an account, you can head to the [Discord developer portal](https://discord.com/developers/applications) to start setting up your bot. Sign in, and once you're at the Applications page, click **New Application** on the top right. The particular name doesn't matter, you could go with something like **CodeDay Discord Bot Workshop** for now. 

After you create your application, navigate to the **Bot** tab and click **Add Bot** and confirm. Keep that tab open, as we'll need to return to invite our bot to our testing server.

## Getting a testing workspace set up

This step is the shortest! It helps to have a space to test your bots in before you release them out onto the wild. If you already have a personal server or a server you share with some friends you don't mind seeing your bot in progress, you can rest easy for now. If not, make a new server and name it whatever you want by hitting the __+__ button at the bottom of Discord's server list.

You'll want to get your bot on the server too. If you didn't, how would we test it? To do this, click the **OAuth2** tab on the Discord developer portal page. Scroll straight down to the box labelled **Scopes** and check the box next to the word **bot**. A new box will appear, providing options for enabling various permissions for our bot. You'll need to examine these carefully when creating other bots, but for now we only need our bot to be able to do one special thing: send messages. So check the box under **Text permissions** that says **Send Messages**. In the box above that says **Scopes**, the URL at the bottom will change; copy this URL, open a new tab in your web browser, and paste it in. Log in to Discord if necessary, and invite it to your testing server. If all goes well, your (as of yet functionless) bot will be added to your server!

# Building the bot!

## What exactly is a bot?

It's good to clarify what exactly a bot is in Discord and what it can do. A bot, in Discord, is essentially like an automated user. The bot can act basically as much as a user can, if the user were omniscient and able to see every event that happened in every server they were in at once. Bots can read messages, send messages, join and play audio in voice channels, send direct messages, give and take roles, and much more, as long as each server it's in gives it permission to do so. We won't get too deep into the capabilities of bots in this workshop, though. What's important to know is that bots are a lot like regular Discord users, but they can do things often a lot better and a lot faster than a human!

## What do we want our bot to be able to do?

There are some really complicated and powerful bots out there -- you may have used some of them! But super complicated bots require super complicated code, and we don't want this to be too overwhelming. So we'll make a simpler bot, but it'll still be able to do something pretty cool! In this case, we'll make a bot that can act as a simple calculator. It'll be able to add, subtract, multiply, and divide numbers, as well as raise them to a given power. When we're finished, you'll be able to invoke it like this:

![bot capabilities]("https://raw.githubusercontent.com/Spirati/discord-workshop/main/img/bot%20capabilities.png")

## Getting started

### Folder structure

Getting a simple bot up and running with discord.py doesn't require a lot of code, but it does require a little bit of setup. Create a new folder somewhere, preferably within something like a projects folder (if you're using repl.it, you have a folder already, so you can skip this), and name it something descriptive. I'll choose `discord-workshop`. Then, make a new file, and name it `main.py`. This file will contain the main code that's necessary to get the bot connected to Discord. You'll also need to make a file named `.env`: this will contain some secret information that we don't want to be publicly viewable in our code if we show it to other people. When everything's set up, you should have a folder setup that's a little like this:

```
projects
| - discord-workshop
    | - main.py
    | - .env
```

### Filling out `.env`

Remember that file we just created called `.env`? That `env` stands for "environment variables": This is basically a long name for pieces of information our computer holds onto for us, often just long enough to run a command (for example, running a script that runs a Discord bot!). These environment variables are hidden from everyone but us, which makes them a good place to keep secret information. There's only one thing we need to put in the environment variables, and that's our bot token.

#### Wait, what's a bot token?

Good question! The bot token is a long string of (more or less) random letters, numbers, and symbols that essentially acts as a password for our bot. It lets Discord know which bot we want to run with our code and also ensures that we have permission to run that bot. This is a dangerous piece of information! If anyone got access to it that you didn't trust with your bot, they could run malicious code while pretending to be your bot! That's why we need to keep it secret in our `.env` file.

#### OK, how do I get my bot token?

This is an easy one: head to the page for your application on the Discord developer portal, and under the **Bot** tab click **Copy** underneath where it says **Token** right next to your bot's profile picture.

Now that you have your bot's token, open up the `.env` file in a text editor (on REPL, you'll just need to click it), and add the following line:

```
WORKSHOP_BOT_TOKEN=token you copied
```

If your token was `example_token`, that'd look like this:

```
WORKSHOP_BOT_TOKEN=example_token
```

### Discord Bot: Beginnings

Now that we have our bot token stored in `.env`, we can make the very beginning of our bot! Open up `main.py` in your text editor of choice, and add the following lines:

```python
import os
import dotenv
import discord.ext.commands as commands

dotenv.load_dotenv()
TOKEN = os.getenv('WORKSHOP_BOT_TOKEN')

bot = commands.Bot(command_prefix='calc!')

bot.run(TOKEN)
```

That's a lot all at once! Let's go through this line by line so we can understand what's happening here.

#### The `import` statements

```python
import os
import dotenv
import discord.ext.commands as commands
```

These three lines all start with `import`: that means they're bringing in some code that someone else wrote into our program. In this case, we're bringing in three different pieces of code, or *modules* (sometimes referred to also as libraries or packages) that all do different things.

- `os` is a library that lets us read certain properties of the operating system we're running our code on. In this case, we're using it to get the environment variable we store our bot token in.
- `dotenv` is from that package we installed at the beginning of the workshop, `python-dotenv`: it finds a file named `.env` in the directory in which you're running your code and copies all of the variables in it to your operating system's environment variables.
- `discord.ext.commands` is a package that makes writing bots in `discord.py` much easier. All of the `.`s in the name indicate that it's a *submodule*: it belongs to and borrows functionality from a larger module, in this case `discord.py`, referred to in code simply as `discord`.

That third line has something special, too: `as commands` is tacked onto the end of our `import` statement. What gives?

Essentially, `as` is a special word in Python that lets us give modules we import shorter or more convenient names. When we run `import os` and `import dotenv`, we can refer to both the `os` and `dotenv` modules in code simply as their names, `os` and `dotenv`. If we made our third line of code simply read `import discord.ext.commands`, we'd have to type `discord.ext.commands` every time we wanted to refer to the `commands` submodule! That's a lot of unnecessary typing, so we give it a shorter name, or *alias* at the top of our code using the `as` keyword, letting us just write `commands` every time we want to refer to `discord.ext.commands`.

#### Getting our bot token

```python
dotenv.load_dotenv()
TOKEN = os.getenv('WORKSHOP_BOT_TOKEN')
```

Lines 5 and 6 deal with grabbing our bot token from our `.env` file and storing it in our code. `dotenv.load_dotenv()` is a *function* that looks at our `.env` file and copies everything in it (in our case, just the `WORKSHOP_BOT_TOKEN` definition) to our OS's environment variables. Functions are essentially named sections of code that let us run a lot of code just by giving the name of the function and adding parentheses `()` at the end.

The next line of code is a *variable assignment*: we're telling our code that we want to store a value (the assignment) under the name `TOKEN` (the variable) so that we can refer to it later. As for the value that gets stored, that goes on the other side of the equals sign; this is another function, just like `dotenv.load_dotenv()`. In this case, `os.getenv` is a function that reads our OS's environment variables and grabs one by its name. The way we tell it which variable to grab is by passing the name of the variable in between the parentheses `()` that indicate that we want to use the `os.getenv` function. When we put information in parentheses like that, they're called *parameters* or *arguments*. In this case, the sole argument is `'WORKSHOP_BOT_TOKEN'`, which indicates that we want the environment variable with that name.

#### Creating and running our bot

```python
bot = commands.Bot(command_prefix='calc!')

bot.run(TOKEN)
```

This first line creates, or *instantiates* our bot using a special kind of function. This function doesn't just give us a value back like `os.getenv` or perform a function behind the scenes like `dotenv.load_dotenv`: it creates a structure that we can use and manipulate, known as a *class*: the word *class* as a whole usually refers to the underlying structure that each copy borrows from, so we call our bot, an individual copy of the `commands.Bot` class, a *class instance* instead. Don't worry too much about the specifics of classes right now; all you need to know is that `bot` refers to a copy of `commands.Bot`, which is a structure that can be used to manipulate Discord bots in code. The `command_prefix='calc!'` part of that line is a *named argument* given to the bot-creating function that tells it it should listen to messages that start with `calc!` to see if they contain commands.

The second line is much simpler! It creates a connection to Discord using our bot token, which lets Discord know which bot to use.

OK, we have our bot code all written out, how do we actually use it and make it so that our bot can come online? That requires running our script, `main.py`. Read the section corresponding to the environment you're working on your code from.

##### REPL

On REPL, this is as simple as hitting the big green play button.

##### Windows

Say your bot's folder is located at `C:\Users\<your_username>\Documents\projects\discord-workshop`. Open up a terminal (`cmd.exe`, Powershell, whatever you prefer). Run these two commands:

- `cd C:\Users\<your_username>\Documents\projects\discord-workshop`

- `python main.py`
  - (If this command doesn't work, try `py main.py`)

##### Linux/macOS

Say your bot's folder is located at one of these locations: `/home/<your_username>/projects/discord-workshop` (most Linux distros) or `/Users/<your_username>/projects/discord-workshop`. Run these two commands:

- `cd /home/<your_username>/projects/discord-workshop` (or the equivalent for your OS)
- `python3 main.py`
  - (If this command doesn't work, try `python main.py`)

#### Uh... nothing happened.

That's a good thing! That means none of our code was malformed. Still, we don't really know what our bot's up to. If you head over to your testing server, you might find that it's displaying as online, but that doesn't tell us a whole lot, and we can't interact with it yet. Let's add a little functionality to our bot that tells us once it's connected to Discord and ready to receive commands. After line 8 of `main.py` (the line that starts with `bot = commands.Bot...`), add the following lines:

```python
@bot.event
async def on_ready():
    print("Connected to Discord!")
 
```

The full structure of `main.py` should now look something like this:

```python
import os
import dotenv
import discord.ext.commands as commands

dotenv.load_dotenv()

bot = commands.Bot(command_prefix="calc!")

@bot.event
async def on_ready():
    print("Connected to Discord!")

bot.run(os.getenv("WORKSHOP_BOT_TOKEN"))
```



 #### What on *earth* does any of that mean??

Now *that* is a very good question. This is a lot of unusual syntax that even longtime users of Python might find novel when first starting with `discord.py`. Let's break it down line-by-line once again.

`@bot.event`

This line tells us that the next couple lines of code are going to fire when our bot notices something happening. The `@` symbol indicates what's known in Python as a *decorator*. It basically indicates that the next section of code, usually a function, is going to have some extra processing done behind the scenes. 

`async def on_ready():`

This line means that we're defining a function. This particular kind of function is what's known as an *event handler*, as it contains the logic responsible for responding to events that our bot notices. Events in `discord.py` have special names that tell us what kinds of events they take care of. In this case, the `on_ready` event fires when our bot connects to Discord and is ready to receive input from users. The `async` keyword essentially means that it's able to run in the background, which lets our bot multitask multiple events and commands at once instead of being forced to handle them one at a time, which would be much slower.

`print("Connected to Discord!")`

This line just puts a little bit of text in the console, in this case telling us that we're connected to Discord. You may also notice that this line is *indented*. In Python, sections of code (often called *blocks*) are separated out through indentation, allowing us to see at a glance what the structure of our code is. 

## Adding functionality: commands and more!

The foundation and base functionality of our bot is done! All that remains is adding the command for running the calculator.