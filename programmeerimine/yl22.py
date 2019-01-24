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
    
    "frankteaexp": input("Frank's tea expences: "),
    "janeteaexp": input("Jane's tea expences: "),
    "frankcofexp": input("Frank's coffee expences: "),
    "janecofexp": input("Jane's coffee expences: "),
}

print(comcalc(dict["franktearev"], dict["frankteaexp"]) + comcalc(dict["frankcofrev"], dict["frankcofexp"]))

print(comcalc(dict["janetearev"], dict["janeteaexp"]) + comcalc(dict["janecofrev"], dict["janecofexp"]))
