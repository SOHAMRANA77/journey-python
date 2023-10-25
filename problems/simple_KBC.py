
questions = ["1: The International Literacy Day is observed on\nA. Sep 8\nB. Nov 28\nC. May 2\nD. Sep 22",
             "2: The language of Lakshadweep.a Union Territory of India,is\nA.Tamil\nB.Hindi\nC.Malayalam \nD.Telugu",
             "3: Bahubali festival is related to\nA. Islam\nB. Hinduism\nC. Buddhism\nD. Jainism",
             "4: Which day is observed as the World Standards  Day?\nA.June 26\nB. Oct 14\nC.Nov 15\nD. Dec 2",
             "5: September 27 is celebrated every year as\nA. Teachers' Day\nB. National Integration Day\nC. World Tourism Day\nD. International Literacy Day",
             "6: Who is the author of 'Manas Ka-Hans' ?\nA.Khushwant Singh\nB.Prem Chand\nC. Jayashankar Prasad\nD. Amrit Lal Nagar",
             "7: Who is the author of the epic \"Meghdoot\"?\nA.Vishakadatta\nB.Valmiki\nC.Banabhatta\nD.Kalidas"]


answer = ["A", "C", "D", "B", "C", "D", "D"]
prize = [1000, 1500, 8000, 16000, 32000, 50000, 80000]
total_prize = 0
lf = 2
current_question = 0
game_on = True
T = "welcome to kaun banega crorepati"
while game_on:
    print(T.upper())
    question = questions[current_question]
    for i in questions:
        print("\n"+i)
        print(answer[current_question])
        A = input("your answer is : ").upper()
        i_l = int(i[0])-1
        if A != answer[i_l]:
            current_question += 1
            if lf > 0:
                print("would you like to use lifeline")
                g_a = input().upper()
                if g_a == "Y":
                    lf -=1
                    continue
            else:
                game_on = False
                break
        else:
            print("\ncongratulation \nNext Question is")
            total_prize += prize[i_l]
            print(f"total life-line you have : {lf} \t\t\t total prize money you have win : {total_prize}")
            current_question += 1
        if current_question == len(questions):
            game_on = False
            break

