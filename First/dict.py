salon = {
    "Company": {
        "BMW": {
            "Model": "Model: M5 CS\nColor: Grey\nPrice: $123.000 to $127.000\nEngine_Displacement: 4.4L\nYear: 2023",
        },
        "Tesla": {
            "Model": "Model: S\nColor: Stealthy Grey\nPrice: $94.990 to $129.990\nEngine_Displacement: -\nYear: 2012",
        },
        "Lamborghini": {
            "Model": "Model: Aventados SVJ\nColor: White\nPrice: $550.000 to $600.000\nEngine_Displacement: 6.5 L\nYear: 2022",
        },
        "Ferrari": {
            "Model": "Model: V6\nColor: Red\nPrice: $338.250 to $373.134\nEngine_Displacement: 3.0 L\nYear: 2021",
        },
        "Chevrolet": {
            "Model": "Model: Cobalt\nColor: White\nPrice: $11.400 to $13.000\nEngine_Displacement: 1.5 L\nYear: 2004",
        }
    }
}

for i in salon["Company"]:
    print(i, end="\n")

user = input("Tallang")

for j in salon["Company"][user]:
    print(j, end="\n")
    print("----------------")

user_n = input("Tallang ")

for n in salon["Company"][user][user_n]:
    print(n, end="")