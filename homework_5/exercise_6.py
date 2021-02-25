from typing import Dict
import re


def sum_all_lesions(_subject: str):
    p_subject = r"[\w]+"
    p_lesions = r"[\d]+"

    def match():
        matched_subject = re.match(p_subject, _subject)
        found_lesions = map(lambda x: int(x), re.findall(p_lesions, _subject))
        if matched_subject and found_lesions:
            return {
                matched_subject.group(0): sum(found_lesions)
            }

    return match()


def count_lesions(filename: str) -> Dict[str, int]:
    vocabulary = dict()  # type: Dict[str, int]
    with open(filename, "r") as file:
        subjects = file.readlines()
        for subject in subjects:
            vocabulary = vocabulary | sum_all_lesions(subject)

    return vocabulary


if __name__ == '__main__':
    print(count_lesions("exercise_6.txt"))
