def find_common_participants(first_group, second_group, separator=','):
    first_group_split = first_group.split(separator)
    second_group_split = second_group.split(separator)

    matches = list(set(first_group_split).intersection(second_group_split))
    matches.sort()

    return matches


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
