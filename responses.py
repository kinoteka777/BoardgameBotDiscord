from random import choice, randint
from datetime import *

# TODO: Add attendees to add_event

def get_response(userInput: str) -> str:
    lowered: str = userInput.lower()

    if lowered == '':
        return "Quiet little mouse aren\'t we...!"
    
    split_message: list[str] = lowered.split(' ')
    command = split_message[0]

    if command =='add_game': # command format: add_game dd-MM 24hr_time game_name
        if len(split_message) >= 4:
            date: datetime = datetime.strptime(split_message[1], '%d-%m').replace(year=datetime.today().year)
            if date < datetime.today():
                return "That date has already passed!"
            time: datetime = datetime.strptime(split_message[2], '%H:%M')
            date = datetime.strftime(date, "%B %d")
            time = datetime.strftime(time, '%I:%M %p')
            game_name: str = split_message[3]

            return f'> **NEW GAME NIGHT!**\n> **GAME**: {game_name.upper()} \n> **DATE**: {date}   **TIME**: {time} \n> BE THERE OR BE SQUARE!'
        else:
            return "Sorry, it seems like your command is incomplete, type 'help' to see a guide to the commands."
        
    elif command == 'help':
        return """> HELP - Displays a list of commands 
                > ADD_GAME - adds a new game event 
                > EXAMPLE - provides an example input for a given command (e.g. example add_game)"""
    
    elif command == 'example':
        if len(split_message) > 1:
            example: str = split_message[1]
            if example == 'add_game':
                return "> **EXAMPLE INPUT: ADD_GAME** \n > >add_game 28-03 21:00 Oceans"
            else:
                return "Sorry, I don\'t recognise that command."

    else:
        return "Type '!help' for a list of commands"