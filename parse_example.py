import argparse
from parser import load_json, load_list_file, analyze_dialog


parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', type=str, metavar='PATH', help='path to the Multi-WOZ corpus', required=True)
args = parser.parse_args()


def main():
    d_dir = args.data_dir

    dialog_data_file = '{}/data.json'.format(d_dir)
    dialog_data = load_json(dialog_data_file)
    dialog_id_list = list(set(dialog_data.keys())) # Bug: v1.0 contains duplicate id in the valid data
    print('# of dialogs:', len(dialog_data))
    # print(dialog_data['PMUL4641.json']) # print a sample dialog

    valid_list_file = '{}/valListFile.json'.format(d_dir)
    test_list_file  = '{}/testListFile.json'.format(d_dir)

    valid_id_list = list(set(load_list_file(valid_list_file))) # Bug: v1.0 contains duplicate id in the valid data
    test_id_list = load_list_file(test_list_file)
    train_id_list = [did for did in dialog_id_list if did not in (valid_id_list + test_id_list)]
    print('# of train dialogs:', len(train_id_list))
    print('# of valid dialogs:', len(valid_id_list))
    print('# of test dialogs :', len(test_id_list))
    assert(len(dialog_id_list) == len(train_id_list) + len(valid_id_list) + len(test_id_list))

    train_data = [v for k, v in dialog_data.items() if k in train_id_list]
    valid_data = [v for k, v in dialog_data.items() if k in valid_id_list]
    test_data = [v for k, v in dialog_data.items() if k in test_id_list]
    assert(len(train_data) == len(train_id_list))
    assert(len(valid_data) == len(valid_id_list))
    assert(len(test_data) == len(test_id_list))

    # print some dialogs with Dialog States
    for d in train_data[:3]:
        print('-' * 50)
        analyze_dialog(d, True)

    hotel_db_list      = load_json('{}/hotel_db.json'.format(d_dir))
    train_db_list      = load_json('{}/train_db.json'.format(d_dir))
    attractin_db_list  = load_json('{}/attraction_db.json'.format(d_dir))
    restaurant_db_list = load_json('{}/restaurant_db.json'.format(d_dir))
    # print(hotel_db_list[0]) # print a sample entity


if __name__ == "__main__":
    main()
