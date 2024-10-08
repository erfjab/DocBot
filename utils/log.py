import logging

def setup_logger(name: str):
    # Create a logger object with the bot's name
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # This can be adjusted as needed

    # Create a file handler for logging to a file
    file_handler = logging.FileHandler(f'{name}.log')
    file_handler.setLevel(logging.INFO)  # Log level for the file

    # Create a formatter that includes the bot name and other relevant details
    formatter = logging.Formatter(f'%(asctime)-25s | {name} | %(levelname)-8s | %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the console and file handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Initialize the logger
logger = setup_logger('DocBot')
