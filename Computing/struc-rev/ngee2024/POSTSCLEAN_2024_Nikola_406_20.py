data = ['1. “Happy #NDP2024 Singapore! #SingaporeNationalDay ”\n',
        '2. “Remembering our journey from 1965 to today. #SGIndependence #NDP2024 ”\n',
        '3. “Unity in diversity – that’s what makes us strong. #TogetherAsOneSG ”\n',
        '4. “Grateful for our frontline heroes who keep us safe. #TogetherAsOneSG #HealthcareHeroes”\n',
        '5. “Red and white forever! #SGPride #SingaporeNationalDay #NDP2024 ”\n',
        '6. “Singapore@Home: Even overseas, we’re connected. #GlobalSG #NDP2024 #SingaporeNationalDay ”\n']

def splitdata(s):
    final = s.lower()
    final = final.split()
    return final

def findtags(data):
    tags = []

    for post in data:
        strings = splitdata(post)
        
        for string in strings:
            if string.startswith("#"):
                if string not in tags:
                    tags.append(string)
                else:
                    continue

    return tags
