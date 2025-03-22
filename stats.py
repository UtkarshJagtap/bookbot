def get_number_of_words(text : str):
    
    all_the_words = text.split()

    print(f"Found {len(all_the_words)} total words")

def get_number_of_characters(text : str):

    results = {}

    for t in text:
        if t.lower() in results:
            results[t.lower()] += 1
        else:
            results[t.lower()] = 1

    return results

def sort_dict(results : dict):
    def sort_on(dict):
        return dict["count"]

    list_of_dict = []
    for key in results:
        res ={
            "character" : key,
            "count": results [key]
        }
        list_of_dict.append(res)

    list_of_dict.sort(reverse=True, key=sort_on)

    for item in list_of_dict:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")

