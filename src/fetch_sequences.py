from Bio import Entrez, SeqIO

Entrez.email = "apoorva.bangalor@ufl.edu"

def fetch_viral_sequences(query, max_records=5):
    handle = Entrez.esearch(db="nucleotide", term=query, retmax=max_records)
    record = Entrez.read(handle)
    ids = record["IdList"]

    fetched = []
    for id_ in ids:
        fetch_handle = Entrez.efetch(db="nucleotide", id=id_, rettype="fasta", retmode="text")
        seq_record = SeqIO.read(fetch_handle, "fasta")
        fetched.append(seq_record)
    return fetched
