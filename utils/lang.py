from enum import Enum

# for next line     : \n
# for bold text     : <b> text </b>
# for mono text     : <code> text </code>
# for use ' in text : \'

class MessageText(str, Enum):
    Start = 'Welcome to my bot'
    Help = 'For use this bot, type @botusername to any chat'