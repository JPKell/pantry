''' These are simple formatting functions that can be used to format strings for html output. '''


def number(number, roundTo=1):
    ''' This function takes a number and returns it as a string with commas separating the thousands. '''
    if isinstance(number, type(None)):
        return None

    if type(number) == str:
        if number.isdecimal() or number.isnumeric():
            number = float(number)

    if roundTo == None:
        return '{:,}'.format(number)
              
    # Check if the number is a float and if the decimal is 0
    if isinstance(number, float) and round(number, roundTo + 1).is_integer():
        number = int(round(number, roundTo + 1))
        return '{:,}'.format(number)
    

    
    # round the number to the number of decimal places specified
    # unless the first number to be cut off is a 5. in that case truncate to the extra decimal place
    number = round(number, roundTo + 1)
    if str(number)[-1] == '5':
        return '{:,}'.format(number)

    number = round(number, roundTo)
    return '{:,}'.format(number)


def currency(number, roundTo=2):
    ''' This function takes a number and returns it as a string with commas separating the thousands and a dollar sign. '''
    # Check if the number is a float and if the decimal is 0
    if type(number) == str:
        if number.isdecimal() or number.isnumeric():
            number = float(number)

    number = round(number, roundTo + 1)
    if str(number)[-1] == '5':
        return '${:,}'.format(number)
    return '${:,.{dp}f}'.format(round(number,roundTo), dp=roundTo)