import random

from src.scrape.scrape_files import scrape_files


def main(src_path, min_examples=20, max_examples=50):
    examples = scrape_files(src_path)
    random.shuffle(examples)
    selected_examples = examples[:max_examples]

    if len(selected_examples) < min_examples:
        print(
            f"Warning: Only {len(selected_examples)} examples generated, which is less than the minimum required {min_examples} examples.")

    for i, (prefix, middle, suffix) in enumerate(selected_examples):
        print(f"Example {i + 1}:\n")
        print(f"Prefix:\n{prefix}\n")
        print(f"Middle:\n{middle}\n")
        print(f"Suffix:\n{suffix}\n")
        print("=" * 40)


if __name__ == "__main__":
    src_path = input("Enter the path to the src folder: ")
    main(src_path)


a = 'E:/Michal/Dokumenty/Projekty/jetbrains/visualization-of-survey-data/src'