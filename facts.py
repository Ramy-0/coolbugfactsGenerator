facts = ['I can see you',
         'one day you will have to answer to your actions and god may not be so merciful',
         'you capitalist scum will never keep the soviet union back forever, we will rise again and you will pay the price',
         'The highest honor in journalism is being murdered by the CIA',
         'Every 60 seconds in Africa a minute passes',
         'UwU',
         "you don't deserve to be happy or feel loved",
         "it's morbin time",
         "AC DC is a great band w kosom ay 7ad y2ol 3aks keda",
         "From the moment I understood the weakness of my flesh, it disgusted me. I craved the strength and certainty of steel. I aspired to the purity of the Blessed Machine. Your kind cling to your flesh, as though it will not decay and fail you",
         'Homosexuality is GAY',
         "if violence isn't solving your problem you are not using enough"]


# def text_format(text):
#     t_list = list(text)
#     if len(t_list) >= 25:
#         for y in range(25, len(t_list), 25):
#             for i in range(y, 0, -1):
#                 if t_list[i] == ' ':
#                     t_list[i] = '\n'
#                     break
#
#     return ''.join(t_list)


def text_format(text):
    endindex = len(text)
    tlist = list(text)

    i = 0
    c = 0
    while True:
        i += 1
        c += 1
        if c == 26:
            while tlist[i] != ' ':
                i -= 1
            tlist[i] = '\n'
            c = 0

        if i >= endindex:
            break

    return ''.join(tlist)

# print(text_format('you capitalist scum will never keep the soviet union back forever, we will rise again and you will pay the price'))
