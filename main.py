from webbrowser import open as browser
class bcolors:
    OK = '\033[92m'  # GREEN
    FAIL = '\033[91m'  # RED
    PROMPT = '\033[93m'  # YELLOW
    RESET = '\033[0m'  # RESET COLOR


def main():
    str = input(bcolors.PROMPT +
                "Enter your text please:\n>> " +
                bcolors.RESET)
    str = convert(str)
    #print("The output is: " +
    #      bcolors.OK +
    #      str)
    browser(str, autoraise=True)

    return 0


def convert(str):
    twitter_init = "https://twitter.com/intent/tweet?text="
    str = str.encode(encoding='UTF-8', errors='strict')
    str = "%s\n" % str
    str = str[2:-2]
    str = str.replace("\\x", "%")
    str = str.replace(" ", "%20")

    return twitter_init + str


if __name__ == "__main__":
    try:
        main()
    except:
        exit()
