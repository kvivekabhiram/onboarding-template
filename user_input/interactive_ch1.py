import time
import validators
import getpass
import os

import fun_visuals, prompts

from clint.textui import colored, puts


def intro():
    """
    simple print introduction
    """

    fun_visuals.twilio_intro()

    time.sleep(.5)

    prompt = 'We are excited to have you join the Twilio team. This is to help start your journey as a Twilio engineer. \n \n' \
             'This text game should start to help you familiarize with common tools and engineering principles ' \
             'here are Twilio. First, lets get acquainted. \n'

    puts(colored.green('{}'.format(prompt)))

    time.sleep(1)

    user_profile()

    return


def user_profile():
    """
    constructs a user profile
    :return:
    """

    pc = prompts.PromptClient()

    # Standard non-empty input
    name = pc._query("What's your name?", validators=[str])

    if name == '' or name is None:
        puts(colored.red('Please enter a name we can call you'))

    # Set validators to an empty list for an optional input
    team = pc._query("What team did you join?", validators=[str])

    title = pc._query("What is your role on the {} team?".format(team), validators=[str])

    # Customized welcome message
    puts(colored.green('\n Hi {}. We are excited to have you as a {} join the {} team! \n'.format(name,
                                                                                                  title,
                                                                                                  team)))

    fun_fact = pc._query("Tell us a fun fact about yourself", validators=[str])

    # construct dictionary of user profile
    user_dict = {
        "name": name,
        "uid": getpass.getuser(),
        "title": title,
        "team": team,
        "fun_fact": fun_fact
    }

    copy(user_profile=user_dict)

    return user_dict


def copy(user_profile):
    """
    copy user_profile
    """

    # get directory
    current_path = os.getcwd()

    # change directory
    os.chdir(current_path + '/funfacts/')

    # check new directory
    new_dir = os.getcwd()

    # create file
    file = new_dir + "/" + user_profile["uid"]

    # write data to file
    f = open(file, "w+")
    f.write(str(user_profile))

    close()

    return


def close():
    """
    close
    """

    puts(colored.green('\n I enjoyed meeting you. \n To see what I have learned about you, '
                       'follow the next steps in the instructions'))

    return



if __name__ == '__main__':
    intro()
