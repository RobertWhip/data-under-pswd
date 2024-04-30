# data-under-pswd

Protect your seed-phrase:
1. Encrypt your seed-phrase: python3 run.py encrypt <your_password> <your_seed_phrase>
2. Decrypt your seed-phrase: python3 run.py decrypt <your_password> <your_hash>


Example:
```
$ python3 run.py encrypt MyFuckingPasswordBliat cats\ fucking\ cats\ fucking\ cats\ fucking\ cats\ fucking\ cats\ fucking\ cats\ fucking
Ciphertext: mSxXihkmLl4mO6ktRkFsU4Oa2FKTb8oSzIaJt5YHN8/76hxIMJGheAF23VHBt7duYAP04CUGGJYG/CG7sPXwVGhHWtkBbvYsxlCIPkpXgIckDj1kQzIgblURnx63qCVGTsVSlAy9tPCRu94XimJihg==

$ python3 run.py decrypt IncorrectPasswordBliat mSxXihkmLl4mO6ktRkFsU4Oa2FKTb8oSzIaJt5YHN8/76hxIMJGheAF23VHBt7duYAP04CUGGJYG/CG7sPXwVGhHWtkBbvYsxlCIPkpXgIckDj1kQzIgblURnx63qCVGTsVSlAy9tPCRu94XimJihg==
ValueError

$ python3 run.py decrypt MyFuckingPasswordBliat mSxXihkmLl4mO6ktRkFsU4Oa2FKTb8oSzIaJt5YHN8/76hxIMJGheAF23VHBt7duYAP04CUGGJYG/CG7sPXwVGhHWtkBbvYsxlCIPkpXgIckDj1kQzIgblURnx63qCVGTsVSlAy9tPCRu94XimJihg==
Decrypted Seed Phrase: cats fucking cats fucking cats fucking cats fucking cats fucking cats fucking

```
