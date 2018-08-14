import os
import json
import global_variables as g


def load_json(data_file):
    if os.path.isfile(data_file):
        with open(data_file, 'r') as read_file:
            data = json.load(read_file)
            return data


def load_list_file(list_file):
    with open(list_file, 'r') as read_file:
        dialog_id_list = read_file.readlines()
        dialog_id_list = [l.strip('\n') for l in dialog_id_list]
        return dialog_id_list
    return


def get_ds_diff(prev_d, crnt_d):
    diff = {}
    # Sometimes, metadata is an empty dictionary, bug?
    if not prev_d or not crnt_d:
        return diff

    for ((k1, v1), (k2, v2)) in zip(prev_d.items(), crnt_d.items()):
        assert k1 == k2
        if v1 != v2: # updated
            diff[k2] = v2
    return diff


def get_domains_by_uttr(dom_list, uttr):
    if len(dom_list) == 1:
        return [dom_list[0]]
    else:
        return [g.UNK_DOM]


def analyze_dialog(d, print_dialog=True):
    assert 'log' in d
    assert 'goal' in d
    domains = []
    # ignore_keys_in_goal = ['eod', 'messageLen', 'message'] # eod (probably) means the user archieved the goal.
    for dom_k, dom_v in d['goal'].items():
        if dom_v and dom_k not in g.ignore_keys_in_goal: # check whether contains some goal entities
            domains.append(dom_k)
    print('{} domain(s): {}'.format(len(domains), domains))

    if print_dialog:
        prev_d = None
        last_usr_uttr = None
        for i, t in enumerate(d['log']):
            spk = 'Usr' if i % 2 == 0 else 'Sys' # Turn 0 is always a user's turn in this corpus.
            if spk == 'Usr':
                last_usr_uttr = t['text']
            elif spk == 'Sys':
                if prev_d is None:
                    prev_d = t['metadata']
                else:
                    crnt_d = t['metadata']
                    ds_diff = get_ds_diff(prev_d, crnt_d)
                    if len(ds_diff.keys()) == 0: # no clues from dialog states
                        crnt_doms = get_domains_by_uttr(domains, last_usr_uttr)
                    else:
                        crnt_doms = ds_diff.keys()
                    for dom_ct, dom_name in enumerate(crnt_doms):
                        print('Domain {}: {}'.format(dom_ct, dom_name))
                    # print('Updated DST:', ds_diff)
                    prev_d = crnt_d
            u = t['text']
            print('{}: {}'.format(spk, u))
