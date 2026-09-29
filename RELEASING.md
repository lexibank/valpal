# Releasing valpal

Recreate the CLDF dataset:

```shell
cldfbench lexibank.makecldf lexibank_valpal.py --glottolog-version v5.3
```

Validate it:
```shell
pytest
```

Create the metadata:
```shell
cldfbench cldfreadme lexibank_valpal.py
```

