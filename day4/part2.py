import re

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    
    card_id = 0
    cards_that_exist = []
    for line in lines:
        line = re.sub("^Card\s*\d+:", "", line).strip()
        winning_numbers_substring = re.match("(^.*)\|", line).group(1).rstrip()
        numbers_i_have_substring = re.match(".*\|(.*$)", line).group(1).strip()
        winning_numbers = [int(match.group(0)) for match in re.finditer("\d+", winning_numbers_substring)]
        numbers_i_have = [int(match.group(0)) for match in re.finditer("\d+", numbers_i_have_substring)]
        winning_numbers_i_have = len(set(winning_numbers) & set(numbers_i_have))
        cards_that_exist.append({"id" : card_id, "matching_num_count" : winning_numbers_i_have})
        card_id += 1

    cards_i_have_unprocessed = cards_that_exist.copy()
    cards_i_have_processed = 0
    while len(cards_i_have_unprocessed) > 0:
        tmp = cards_i_have_unprocessed
        cards_i_have_unprocessed = []
        for card in tmp:
            cards_i_have_processed += 1
            if "memoized_result" not in card:
                card["memoized_result"] = []
                if card["matching_num_count"] > 0:
                    for i in range(card["id"] + 1, card["id"] + card["matching_num_count"] + 1):
                        if i < len(cards_that_exist):
                            card["memoized_result"].append(cards_that_exist[i])
            cards_i_have_unprocessed.extend(card["memoized_result"])
    print(cards_i_have_processed)

