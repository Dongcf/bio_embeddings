# Bio Embeddings
The project includes:

- A pipeline that allows to embed a FASTA file choosing from various embedders (see below), and then project and visualize the embeddings on 3D plots.
- General purpose library to embed protein sequences in any python app.
- A web server that takes in sequences, embeds them and returns the embeddings OR visualizes the embedding spaces on interactive plots online.

We presented the bio_embeddings pipeline as a talk at ISMB 2020. You can [find the talk on YouTube](https://www.youtube.com/watch?v=NucUA0QiOe0&feature=youtu.be), and [the poster on F1000](https://f1000research.com/posters/9-876).

## News (current development cycle)

- Develop now includes new models from [ProtTrans](https://doi.org/10.1101/2020.07.12.199554). The models are `albert`, `bert` and `xlnet`. They will officially be included in release `0.1.4`, but can be installed by installing the pipeline from GitHub (see _Install Guides_)
- Release `0.1.4` will be installable on Google Colab (thanks to Prof. Georgina Stegmayer for helpful input). In the meantime:
    - [Check out this Google Colab](https://colab.research.google.com/drive/1msZVwcCT2b768HnbRK3SrnmRqtVjvsgg?usp=sharing) allows you to extract features (secondary structure and protein localization) from a FASTA formatted sequence file (directly on Google hardware; **FAST** even if you don't have a GPU on your computer!!).
  - [Check out this other Google Colab](https://colab.research.google.com/drive/1h5izTF07GjHMkekmGNUj32Sbb1gccJxd?usp=sharing) to get embeddings for sequences in a FASTA file (you can then download them and use them as input features for prediction models).
- Release `0.1.4` will include embedding similarity transfer and supervised annotation extraction via a new stage called `extract`.

## Cite

While we are working on a proper publication, if you are already using this tool, we would appreciate if you could cite the following poster:

> Dallago C, Schütze K, Heinzinger M et al. bio_embeddings: python pipeline for fast visualization of protein features extracted by language models [version 1; not peer reviewed]. F1000Research 2020, 9(ISCB Comm J):876 (poster) (doi: [10.7490/f1000research.1118163.1](https://doi.org/10.7490/f1000research.1118163.1))

## Install guides

You cam install bio_embeddings with pip or use it through docker

## Pip

You can install the pipeline via pip like so:

```bash
pip install bio-embeddings[all]
```

To get the latest features, please install the pipeline like so:

```bash
pip install -U "bio-embeddings[all] @ git+https://github.com/sacdallago/bio_embeddings.git"
```

### Docker

We will provide a docker image at `rostlab/bio_embeddings`. Simple usage example:

```shell_script
docker run --rm --gpus all \
    -v "$(pwd)/examples/docker":/mnt \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    rostlab/bio_embeddings /mnt/config.yml
```

See the docker example in the examples folder for instructions. We currently have published `rostlab/bio_embeddings:develop`. For our next stable release, we will publish tags for all releases and a `latest` tag pointing to the latest release.

## What model is right for you?

Each models has its strengths and weaknesses (speed, specificity, memory footprint...). There isn't a "one-fits-all" and we encourage you to at least try two different models when attempting a new exploratory project.

The models `albert`, `bert`, `seqvec` and `xlnet` were all trained with the goal of systematic predictions. From this pool, we believe the optimal model to be `bert`, followed by `seqvec`, which has been established for longer and uses a different principle (LSTM vs Transformer).

## Examples

We highly recommend you to check out the `examples` folder for pipeline examples, and the `notebooks` folder for post-processing pipeline runs and general purpose use of the embedders.

After having installed the package, you can:

1. Use the pipeline like:

    ```bash
    bio_embeddings config.yml
    ```

    A blueprint of the configuration file, and an example setup can be found in the `examples` directory of this repository.

1. Use the general purpose embedder objects via python, e.g.:

    ```python
    from bio_embeddings.embed import SeqVecEmbedder

    embedder = SeqVecEmbedder()

    embedding = embedder.embed("SEQVENCE")
    ```

    More examples can be found in the `notebooks` folder of this repository.

## Development status


<details>
<summary>Pipeline stages</summary>
<br>

- embed:
  - [x] Bert (https://doi.org/10.1101/2020.07.12.199554)
  - [x] SeqVec (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3220-8)
  - [x] Albert (https://doi.org/10.1101/2020.07.12.199554)
  - [x] XLNet (https://doi.org/10.1101/2020.07.12.199554)
  - [ ] Fastext
  - [ ] Glove
  - [ ] Word2Vec
  - [x] UniRep (https://www.nature.com/articles/s41592-019-0598-1)
- project:
  - [x] t-SNE
  - [x] UMAP
- extract:
  - supervised:
    - [x] SeqVec: DSSP3, DSSP8, disorder, subcellular location and membrane boundness as in https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3220-8
    - [x] Bert: DSSP3, DSSP8, disorder, subcellular location and membrane boundness as in https://doi.org/10.1101/2020.07.12.199554
</details>

<details>
<summary>Web server (unpublished)</summary>
<br>

- [x] SeqVec
- [x] Albert (https://doi.org/10.1101/2020.07.12.199554)
</details>

<details>
<summary>General purpose embedders</summary>
<br>

- [x] SeqVec (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3220-8)
- [x] Fastext
- [x] Glove
- [x] Word2Vec
- [x] UniRep (https://www.nature.com/articles/s41592-019-0598-1)
- [x] Albert (https://doi.org/10.1101/2020.07.12.199554)
- [x] Bert (https://doi.org/10.1101/2020.07.12.199554)
- [x] XLNet (https://doi.org/10.1101/2020.07.12.199554)
</details>

## Building a Distribution
Building the packages best happens using invoke.
If you manage your dependencies with poetry this should be already installed.
Simply use `poetry run invoke clean build` to update your requirements according to your current status
and to generate the dist files

### Additional dependencies and steps to run the webserver

If you want to run the webserver locally, you need to have some python backend deployment experience.
You'll need a couple of dependencies if you want to run the webserver locally: `pip install dash celery pymongo flask-restx pyyaml`.

Additionally, you will need to have two instances of the app run (the backend and at least one celery worker), and both instances must be granted access to a MongoDB and a RabbitMQ or Redis store for celery.

## Contributors

- Christian Dallago (lead)
- Konstantin Schütze
- Tobias Olenyi
- Michael Heinzinger
