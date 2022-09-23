from src.equation import ari_function, count_characters, count_sentences, count_words, quantify_ari

INDEX = 1

def main():
    """Main function."""

    filename: list[str] = ["test_text.txt", "gettysburg_address.txt"]

    with open(filename[INDEX], "r") as file:
        text = file.read()


    words = count_words(text)
    characters = count_characters(text)
    sentences = count_sentences(text)

    # print(f"Words: {words}")
    # print(f"Sentences: {sentences}")
    # print(f"Characters: {characters}")

    ari = ari_function(words, characters, sentences)

    print(f"The ARI for {filename[INDEX]} is {ari}.")
    print(f"This corresponds to a {quantify_ari(ari)['grade_level']} level of difficulty")
    print(f"that is suitable for an average person {quantify_ari(ari)['ages']} years old.")

if __name__ == "__main__":
    main()