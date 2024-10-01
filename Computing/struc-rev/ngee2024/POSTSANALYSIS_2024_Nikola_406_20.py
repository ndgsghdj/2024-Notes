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

def count_tags(tags, data):
    count = {c:0 for c in tags}

    for post in data:
        string = splitdata(post)
        for word in string:
            if word in tags:
                count[word] += 1

    count_list = []

    for tag in count:
        count_list.append(count[tag])

    return count_list

tags = findtags(data)
count_list = count_tags(tags, data)
top_2 = []
top_2_counts = []

i = 0

while True:
    if len(top_2) == 2:
        break
    if count_list[i] == max(count_list):
        top_2.append(tags[i])
        top_2_counts.append(count_list[i])
        count_list.pop(i)
        tags.pop(i)
        i = 0
    else:
        i += 1

print("The top 2 tags are {}".format(", ".join(top_2)))

top_2_counts = [str(k) for k in top_2_counts]

print("The number of times are {}".format(", ".join(top_2_counts)))
