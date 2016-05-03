# preset paragraphs and answers
paragraph_easy = '''
A wolf had been badly wounded by dogs. He lay sick and maimed in his lair.
He felt very __1__ and thirsty. When a sheep passed by, he __2__ him to
fetch some __3__ from the stream.

"If you bring me the __3__," he said, "I will find means to get some food."

"Yes," said the sheep, "if I bring you the __3__, you would undoubtedly
make me your __4__."
'''

easy_answers = ['hungry', 'asked', 'water', 'food']

paragraph_medium = '''
A man wanted to buy an ass. He went to the market, and saw a likely one.
But he wanted to test him first.

So he took the ass home, and put him into the stable with the other asses.
The new ass looked around, and immediately went to choose a place next to
the laziest ass in the stable.

When the man saw this he put a __1__ on the ass at once, and gave him back
to his __2__.

The __2__ felt quite surprised. He asked the man, "Why are you back so soon?
Have you tested him already?" "I don't want to test him any more," replied
the man, "From the __3__ he chose for himself, I could see what sort of
__4__ he is."
'''

medium_answers = ['halter', 'owner', 'companion', 'animal']

paragraph_hard = '''
Swift is a general-purpose, multi-paradigm, compiled programming language
created for __1__, OS X, watchOS, tvOS and Linux development by Apple Inc.
Swift is designed to work with Apple's Cocoa and Cocoa Touch frameworks and
the large body of existing __2__ code written for Apple products. Swift is
intended to be more resilient to erroneous code ("safer") than __2__ and
also more concise. It is built with the LLVM compiler framework included in
Xcode 6 and later and uses the __2__ runtime, which allows C, __2__,
C++ and Swift code to run within a __3__ program.

Swift supports the core concepts that made __2__ flexible, notably dynamic
dispatch, widespread late binding, extensible programming and similar features.
These features also have well known performance and safety trade-offs, which
Swift was designed to address. For safety, Swift introduced a system that helps
address common programming __4__ like null pointers, as well as introducing
syntactic sugar to avoid the pyramid of doom that can result. For performance
issues, Apple has invested considerable effort in aggressive optimization that
can flatten out method calls and accessors to eliminate this overhead. More
fundamentally, Swift has added the concept of protocol extensibility, an
extensibility system that can be applied to types, structs and classes. Apple
promotes this as a real change in programming paradigms they refer to as
"__5__-oriented programming".
'''

hard_answers = ['iOS', 'Objective-C', 'single', 'errors', 'protocol']


# get the user input for difficulty
def get_difficulty():
    menu = '''Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.\n'''
    user_input = raw_input(menu).lower()
    return user_input


# remind the user what difficulty has been chosen
def difficulty_reminder(d):
    return "You've chosen " + d + '!\n'


# remind the user the number of guesses in current problem
def guesses_num_reminder(n):
    return 'You will get ' + str(n) + ' guesses in this problem.'


# remind the user the number of chances in current problem
def chances_num_reminder(n):
    return 'For each guess, you will have ' + str(n) + ' chances to try. Good luck!\n'


# combine the information above and print them
def show_reminder(difficulty, guesses_num, chances_num):
    print difficulty_reminder(difficulty)
    print guesses_num_reminder(guesses_num)
    print chances_num_reminder(chances_num)


# check if the blank is in a given word
def blank_in_word(blank, word):
    if blank in word:
        return blank
    return None


# replace the blank with the answer in a given paragraph
def replace_the_blank(paragraph, blank, answer):
    words_list = paragraph.splitlines()
    for word in words_list:
        result = blank_in_word(blank, word)
        if result:
            words_list[words_list.index(word)] = word.replace(result, answer)
    replaced = '\n'.join(words_list) + '\n'
    return replaced


# print the current paragraph with some style
def prt_current_paragraph(paragraph):
    paragraph_mark_start = '#' * 19 + ' The current paragraph reads as such: ' + '#' * 19
    paragraph_mark_end = '#' * 76
    print paragraph_mark_start
    print paragraph
    print paragraph_mark_end
    print ''


# get the user input for an answer
def get_answer(blank):
    user_input = raw_input('What should be substituted in for' + blank + '?')
    return user_input


# process while the answer that user give is wrong
def process_wrong_answer(answer_input, paragraph, p_index, blank, chances_num, guess_index, chance_index):
    while answer_input.lower() != answers_list[p_index][guess_index].lower() and chance_index < chances_num:
        incorrect = "That isn't the correct answer! "
        message_style1 = "Let's try again; you have " + str(chances_num - chance_index) + ' trys left!\n'
        message_style2 = 'You only have 1 try left! Make it count!\n'

        if chances_num - chance_index > 1:
            print incorrect + message_style1
        else:
            print incorrect + message_style2

        prt_current_paragraph(paragraph)
        answer_input = get_answer(blank)
        chance_index += 1
        if chance_index == chances_num:
            print "You've failed too many straight guesses! Game Over!"
            exit()


# process what will the paragraph look like depending on the answer
def process_paragraph(paragraph, p_index, guesses_num, chances_num):
    for i in range(0, guesses_num):
        prt_current_paragraph(paragraph)

        blank = blanks[i]
        answer = answers_list[p_index][i]
        answer_input = get_answer(blank)

        j = 1
        process_wrong_answer(answer_input, paragraph, p_index, blank, chances_num, i, j)

        # process while the answer is correct
        if answer_input.lower() == answers_list[p_index][i].lower():
            print 'Correct!\n'
            paragraph = replace_the_blank(paragraph, blank, answer)

    prt_current_paragraph(paragraph)
    print 'You won!'
    exit()


# process what paragraph will be dealt with depending on the difficulty
def process_difficulty_mode(para_list, dfct_input, dfct_opts, dfct_short_opts, guesses_num_opts, chances_num_opts):
    for i in range(0, len(paragraphs_list)):
        if dfct_input == dfct_opts[i] or dfct_input == dfct_short_opts[i]:
            d = dfct_opts[i]
            g = guesses_num_opts[i]
            c = chances_num_opts[i]
            show_reminder(d, g, c)
            process_paragraph(para_list[i], i, g, c)


# preset variables
paragraphs_list = [paragraph_easy, paragraph_medium, paragraph_hard]
answers_list = [easy_answers, medium_answers, hard_answers]
blanks = ['__1__', '__2__', '__3__', '__4__', '__5__']
difficulty_options = ['easy', 'medium', 'hard']
difficulty_short_options = ['e', 'm', 'h']
guesses_num_options = [4, 4, 5]     # from left to right represent the number of guesses in each problem
chances_num_options = [5, 5, 5]     # from left to right represent the number of chances for a guess in each problem

# continuing ask the user to input difficulty while input is wrong
difficulty_input = get_difficulty()
while difficulty_input not in difficulty_options and difficulty_input not in difficulty_short_options:
    print "That's not an option!"
    difficulty_input = get_difficulty()

# once a difficulty has been chosen, run this function to go on
process_difficulty_mode(paragraphs_list, difficulty_input, difficulty_options, difficulty_short_options,
                        guesses_num_options, chances_num_options)
