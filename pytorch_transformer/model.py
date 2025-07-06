import torch
import torch.nn as nn
import math

class InputEmbeddings(nn.Module):
    def __init__(self, d_model: int, vocab_size:int):
        super().__init__()
        self.d_model=d_model,
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size,d_model)

    def forwad(self,x):
        return self.embedding(x) * math.sqrt(self.d_model)

class PostionalEncoding(nn.Module):
    def __init__(self,d_model: int, seq_lnt: int, dropout: float)->None:
        super().__init__()
        self.d_model = d_model
        self.seq_lnt = seq_lnt
        self.dropout = nn.Dropout(dropout)

        # Create a matrix of shape(seq_lnt, d_model); i.e nothing but matrix of sentences and it's token embeddings
        pe= torch.zeroes(seq_lnt,d_model)
        # Now lets create a vector os size (seq_lnt)
        