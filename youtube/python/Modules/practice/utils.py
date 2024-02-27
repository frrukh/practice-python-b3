def find_max(number):
    (maximum)=number[0]
    for item in number:
        if maximum<item:
            maximum=item
    return(maximum)
