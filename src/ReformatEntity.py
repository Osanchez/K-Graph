class ReformatEntity:

    @staticmethod
    def reformat_file(directory, new_file_name):
        number_lines = 0
        with open(directory, 'r') as r:
            with open(new_file_name, 'w') as w:
                for line in r:
                    number_lines += 1
                    read_line = line.strip('\n')
                    w.write(read_line)
                    w.write('\n')
                w.write(str(number_lines))


def main():
    entity2id_directory = "../doc/FB15K/entity2id.txt"
    relation2id_directory = "../doc/FB15K/relation2id.txt"
    test_directory = "../doc/FB15K/test.txt"
    train_directory = "../doc/FB15K/train.txt"
    valid_directory = "../doc/FB15K/valid.txt"

    reformat = ReformatEntity()
    reformat.reformat_file(entity2id_directory, "entity2id.txt")

    reformat = ReformatEntity()
    reformat.reformat_file(relation2id_directory, "relation2id.txt")

    reformat = ReformatEntity()
    reformat.reformat_file(test_directory, "test2id.txt")

    reformat = ReformatEntity()
    reformat.reformat_file(train_directory, "train2id.txt")

    reformat = ReformatEntity()
    reformat.reformat_file(valid_directory, "valid2id.txt")


if __name__ == "__main__":
    main()
