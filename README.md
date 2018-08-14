:construction:  This parser is in the middle of development.

# MultiWOZ-Parser (Unofficial)
A parser of the Multi-Domain Wizard-of-Oz dataset (MultiWOZ). The dataset consists of 2,730 single-domain dialogues that include booking if the domain allows for that and 7,375 multi-domain dialogues consisting of at least 2 up to 5 domains.

> MultiWOZ - A Large-Scale Multi-Domain Wizard-of-Oz Dataset for Task-Oriented Dialogue Modelling
> Budzianowski, Pawe{\l} and Wen, Tsung-Hsien and Tseng, Bo-Hsiang  and Casanueva, I{\~n}igo and Ultes Stefan and Ramadan Osman and Ga{\v{s}}i\'c, Milica. EMNLP 2018.
> URL will be available.

> Large-Scale Multi-Domain Belief Tracking with Knowledge Sharing.
> Osman Ramadan, Paweł Budzianowski, Milica Gašić. ACL 2018.
> https://arxiv.org/abs/1807.06517

## Dataset
You can download the dataset [here](http://dialogue.mi.eng.cam.ac.uk/index.php/corpus/).

## Parsers
There are two types of the parser; _iptyhon_ and _python_. Basically, they are the same and you can see some data processing flow and some sample data.

## How to use the parser?

```
python main.py --data_dir ./MultiWOZ/
```
