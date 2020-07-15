import tempfile

from bio_embeddings.embed.albert_embedder import AlbertEmbedder as _AlbertEmbedder
from bio_embeddings.embed.bert_embedder import BertEmbedder as _BertEmbedder
from bio_embeddings.embed.embedder_interface import EmbedderInterface
from bio_embeddings.embed.fasttext_embedder import FastTextEmbedder as _FastTextEmbedder
from bio_embeddings.embed.glove_embedder import GloveEmbedder as _GloveEmbedder
from bio_embeddings.embed.seqvec_embedder import SeqVecEmbedder as _SeqVecEmbedder
from bio_embeddings.embed.short_albert_embedder import ShortAlbertEmbedder as _ShortAlbertEmbedder
from bio_embeddings.embed.word2vec_embedder import Word2VecEmbedder as _Word2VecEmbedder
from bio_embeddings.embed.xlnet_embedder import XLNetEmbedder as _XLNetEmbedder
from bio_embeddings.utilities.remote_file_retriever import get_model_file, get_model_directories_from_zip

_temporary_files = list()


# To make it easier for end-users of the embeddings as a package,
# auto-download missing files!


class SeqVecEmbedder(_SeqVecEmbedder):

    def __init__(self, **kwargs):
        necessary_files = ['weights_file', 'options_file']

        if kwargs.get('seqvec_version') == 2 or kwargs.get('vocabulary_file'):
            necessary_files.append('vocabulary_file')
            kwargs['seqvec_version'] = 2

        for file in necessary_files:
            if not kwargs.get(file):
                f = tempfile.NamedTemporaryFile()
                _temporary_files.append(f)

                get_model_file(path=f.name, model='seqvecv{}'.format(str(kwargs.get('seqvec_version', 1))), file=file)

                kwargs[file] = f.name
        super().__init__(**kwargs)


class AlbertEmbedder(_AlbertEmbedder):

    def __init__(self, **kwargs):
        necessary_directories = ['model_directory']

        for directory in necessary_directories:
            if not kwargs.get(directory):
                f = tempfile.mkdtemp()
                _temporary_files.append(f)

                get_model_directories_from_zip(path=f, model='albert', directory=directory)

                kwargs[directory] = f
        super().__init__(**kwargs)


class ShortAlbertEmbedder(_ShortAlbertEmbedder):

    def __init__(self, **kwargs):
        necessary_directories = ['model_directory']

        for directory in necessary_directories:
            if not kwargs.get(directory):
                f = tempfile.mkdtemp()
                _temporary_files.append(f)

                get_model_directories_from_zip(path=f, model='albert_short', directory=directory)

                kwargs[directory] = f
        super().__init__(**kwargs)


class BertEmbedder(_BertEmbedder):

    def __init__(self, **kwargs):
        necessary_directories = ['model_directory']

        for directory in necessary_directories:
            if not kwargs.get(directory):
                f = tempfile.mkdtemp()
                _temporary_files.append(f)

                get_model_directories_from_zip(path=f, model='bert', directory=directory)

                kwargs[directory] = f
        super().__init__(**kwargs)


class XLNetEmbedder(_XLNetEmbedder):

    def __init__(self, **kwargs):
        necessary_directories = ['model_directory']

        for directory in necessary_directories:
            if not kwargs.get(directory):
                f = tempfile.mkdtemp()
                _temporary_files.append(f)

                get_model_directories_from_zip(path=f, model='xlnet', directory=directory)

                kwargs[directory] = f
        super().__init__(**kwargs)


class Word2VecEmbedder(_Word2VecEmbedder):
    def __init__(self, **kwargs):
        necessary_files = ['model_file']

        for file in necessary_files:
            if not kwargs.get(file):
                f = tempfile.NamedTemporaryFile()
                _temporary_files.append(f)

                get_model_file(path=f.name, model='word2vec', file=file)

                kwargs[file] = f.name

        super().__init__(**kwargs)


class FastTextEmbedder(_FastTextEmbedder):
    def __init__(self, **kwargs):
        necessary_files = ['model_file']

        for file in necessary_files:
            if not kwargs.get(file):
                f = tempfile.NamedTemporaryFile()
                _temporary_files.append(f)

                get_model_file(path=f.name, model='fasttext', file=file)

                kwargs[file] = f.name

        super().__init__(**kwargs)


class GloveEmbedder(_GloveEmbedder):
    def __init__(self, **kwargs):
        necessary_files = ['model_file']

        for file in necessary_files:
            if not kwargs.get(file):
                f = tempfile.NamedTemporaryFile()
                _temporary_files.append(f)

                get_model_file(path=f.name, model='glove', file=file)

                kwargs[file] = f.name

        super().__init__(**kwargs)
