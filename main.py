from src.slack_bot.slack_bot import slackbot_main
import logging

# defining log file:
def config_logging(number):
    # create a directory for logging
    log_dir = "log"
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname:<8} {message}",
        style="{",
        filename="./log/%d.log" % number,
        filemode="a",
        force=True,
    )

config_logging(0)

if __name__ == "__main__":
    slackbot_main()