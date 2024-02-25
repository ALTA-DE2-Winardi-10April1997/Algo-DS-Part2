def count_item_and_sort(items):
    result = ""
    count_items = {}
    for item in items:
        if item in count_items:
            count_items[item] += 1
        else:
            count_items[item] = 1

    sorted_count = sorted(count_items.items(), key=lambda x: (x[1], x[0]))
    result = " ".join([f"{key}->{value}" for key, value in sorted_count])
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"