# program to display the lastname of the second employee and the firstname of the owners

company = {
  "employees":[{"firstName" : "John", "lastName" : "Doe"},
                {"firstName" : "Anna", "lastName" : "Smith"}, 
                {"firstName" : "Peter", "lastName" : "Jones"}],

  "owners":[{"firstname": "Jack", "lastName": "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]
    }

print(company["employees"][1]['lastName'])
print(company["owners"][0]['firstname'])
