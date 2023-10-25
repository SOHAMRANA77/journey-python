import os


def q_a(i):
    """Q = q_a(1)   print(Q[0])"""
    q = [["Among the following actors, which actor is commonly recognized as the “Angry Young Man”?",
          "A. Shah Rukh Khan", "B. Saif Ali Khan", "C. John Abrahim", "D. Amitabh Bachchan", "D"],
         ["The film industry of India is mottled for its underworld acquaintances. Among the following people, "
          "who was killed by the underworld thugs?",
          "A. Sanjeev Kumar", "B. Divya Bharti", "C. Gulshan Kumar", "D. Vinod Mehra", "C"],
         ["This movie was based on a Cricket match and was admired by people all around the world. It was nominated "
          "as the Best Foreign Film at Oscars in the year 2001. Identify the movie.",
          "A. Refugee", "B. Mohabbatein", "C. Badal", "D. Lagaan", "D"],
         ["Among the following actresses, the Lux New Face award of the year 1997 was bagged by?",
          "A. Aishwarya Rai", "B. Mahima Chowdhary", "C. Rani Mukherjee", "D. Sushmita Sen", "B"],
         ["The songs of Raj Kapoor’s movie were always a super hit. One of the blockbuster Raj Kapoor films was the "
          "movie 'Bobby'. Can you identify the music director of this film?",
          "A. Adnan Sami", "B. Anand Raj Anand", "C. Anil Biswas", "D. Laxmikant-Pyarelal", "D"],
         ["One of the greatest movies of Bollywood is 'Mughal-E-Azam'. Can you name the music director of this movie?",
          "A. Arjun Janya", "B. Anoop Seelin", "C. Naushad Ali", "D. Devarajan", "C"],
         ["The story of the movie ‘Hello’, directed by Atul Agnihotri, was adapted from which famed novel?",
          "A. One Night at the Call Center", "B. The God of Small Things", "C. The White Tiger", "D. Midnight’s "
                                                                                                 "Children", "A"],
         ["\"Itna sannata kyun hai bhai?\"is a very famous dialogue.  Who said these famous words in the movie Sholay?",
          "A. Dharmendra", "B. Sanjeev Kumar", "C. Amjad Khan", "D. A. K. Hangal", "D"],
         ["Which is India's first indigenously made Colour film?",
          "A. Bachpan", "B. Baarish", "C. Kisan Kanya", "D. Badshah", "C"],
         ["This Bollywood star was chosen as one of the jury members for the Cannes Film Festival in 2003?",
          "A. Aishwarya Rai", "B. Saif Ali Khan", "C. John Abrahim", "D. Amitabh Bachchan", "A"],
         ["Which country won the final series of the triangular Cricket series that took place in Durban in February "
          "1997?",
          "A. Australia", "B. South Africa", "C. India", "D. Pakistan", "C"],
         ["India played its First 1 - day international match in?”?",
          "A. Headingley", "B. Lords", "C. Oval", "D. Green park", "A"],
         ["India became victorious in the World Cricket Championship beating Pakistan in the final by Eight wickets. "
          "Who won the man of the tournament title?",
          "A. Sachin Tendulkar", "B. Ravi Shastri", "C. Saurav Ganguly", "D. Ajay Jadeja", "B"],
         ["The first ODI captain for India was?",
          "A. C K Nayadu", "B. Vinoo Mankad", "C. Ajit Wadekar", "D. Lala Amarnath", "C"],
         ["The first ODI match was played in India in?",
          "A. Ahmedabad", "B. Lucknow", "C. Kanpur", "D. Kolkata", "A"],
         ["The first president of BCCI (Board of Control for Cricket in India) was?",
          "A. M. A. Chidambaram", "B. Z. R. Irani", "C. Ramprakash Mehra", "D. R.E. Grant Govan", "D"],
         ["Among the following movies, which one is not directed by Mr. V. Shantaram?",
          "A. Stree", "B. Razia Sultan", "C. Geet Gaya Patharon Ne", "D. Amar Bhoopali", "B"],
         ["She made her debut film along with the renowned actor Raj Kapoor with the movie 'Neel Kamal'?",
          "A. Aamani", "B. Anita Raj", "C. Bindu", "D. Madhubala", "D"]
         ]
    # print(len(q))
    return q[i]


cash = 0
prize_money_structure = [
    1000,  # First Question
    2000,  # Second Question
    3000,  # Third Question
    5000,  # Fourth Question
    10000,  # Fifth Question
    20000,  # Sixth Question
    40000,  # Seventh Question
    80000,  # Eighth Question
    160000,  # Ninth Question
    320000,  # Tenth Question
    640000,  # Eleventh Question
    1250000,  # Twelfth Question
    2500000,  # Thirteenth Question
    5000000,  # Fourteenth Question
    10000000,  # Fifteenth Question (1 crore)
    70000000  # Top Prize (7 crores)
]
Rlen = 16
Q_n = 0
LL = 3
life = ["Audience Poll", "50%50", "Phone-A-Friend"]
game_on = True
print("welcome to kaun banega crorepati".upper())
while game_on:

    if LL == 0:
        print("Question Value = ", prize_money_structure[Q_n])
    else:
        print("Question Value = ", prize_money_structure[Q_n], "\t\t\t\t\t\t\tLife line left = ", LL)
    Q = q_a(Q_n)
    os.system('cls')
    # Extract the question, answer choices, and correct answer
    question = Q[0]
    options = Q[1:5]
    correct_answer = Q[5]

    # Display the question and answer choices
    print(f"{Q_n + 1}, {question}")
    for option in options:
        print("\t" + option)

    # Display the correct answer
    print("Correct Answer:", correct_answer)
    print("\tfor life line enter \"L\"") if LL >= 1 else print("No life line")
    A = input("\tEnter Your Answer = ").upper()
    if A == "L":
        if LL < 1:
            continue

        if 1 <= LL <= 3:
            LL -= 1
            continue
    elif A == correct_answer:

        Q_n += 1
        Rlen -= 1
        if Rlen == 0:
            print("Game is over ""\n prize you win is ", cash, "$")
            break
        print("\ncongratulation \nNext Question is")
        cash += prize_money_structure[Q_n]
    elif A == "Q":
        print(cash)
        break

