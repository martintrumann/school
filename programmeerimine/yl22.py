def comcalc(rev, exp):
    tot = int(rev) - int(exp)

    if tot < 0:
        commision = 0
    else:
        commision = tot * 0.062
    return commision

dict = {
    "franktearev": input("Frank's tea revenue: "),
    "janetearev": input("Jane's tea revenue: "),
    "frankcofrev": input("Frank's coffee revenue: "),
    "janecofrev": input("Jane's coffee revenue: "),
    
    "frankcofexp": input("Frank's coffee expences: "),
    "janecofexp": input("Jane's coffee expences: "),
    "janeteaexp": input("Jane's tea expences: "),
    "frankteaexp": input("Frank's tea expences: "),
}

print(comcalc(dict["franktearev"], dict["frankteaexp"]))

print(comcalc(dict["janetearev"], dict["janeteaexp"]))

print(comcalc(dict["frankcofrev"], dict["frankcofexp"]))

print(comcalc(dict["janecofrev"], dict["janecofexp"]))
