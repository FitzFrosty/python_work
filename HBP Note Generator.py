#Make this a form
#make this import the well listing tab
#make it ask if formations are misspelled


while True:
    operator = input("Who is the operator?")
    well_name = input("What is the Well name?")
    location = input("What is the Surface location?")
    spud_date = input("When is the spud date")
    formations = input("Which formations is it producing from?")
    unit_size = input("What is the unit size?")
    total_depth = input("What is the total depth?")
    lwd = input('When did the well last report production?')


    print('HBP by ' + operator + "'s, " + well_name + ', ' + location + ', spud ' + spud_date
      + ', ' + formations + ', ' + unit_size + ', TD ' + total_depth + "', LWD " +
      lwd + '.')

