# 🦠 Viral Genomics with Biopython: Dengue Case Study

This project uses [Biopython](https://biopython.org/) to create a reproducible pipeline for exploring viral genomes, running BLAST queries, performing multiple sequence alignment, and building phylogenetic trees. 
The viral genome analysis is done using public databases and bioinformatics tools, designed to be understandable to be users with no background in Biology.
An example is demonstrated on **Dengue virus** genome sequences.

## 🧬 What is a Virus?

A virus is a tiny infectious agent that can only reproduce by invading the cells of a host organism. It’s made up of:

* A genome — either DNA or RNA letters (A, T/U, C, G) that make up the genetic material

* A protein coat that protects the genome

* Sometimes a lipid envelope (in some viruses)

This project focuses on viral genome sequences that carry all of a virus’s biological instructions.

🧬 Example: Structure of a Virus

       [ Genome ]
          |
     +-------------+
     |  Protein    |
     |   Coat      |   ← Capsid
     +-------------+
        / \
     (Optional) Envelope

  Genome: RNA or DNA (e.g., Dengue is RNA)

## 🧬 Project Features

### 🧪 Fetch Viral Genomes from NCBI Entrez
Connects to NCBI (National Center for Biotechnology Information) Entrez using Biopython to download virus genome sequences in FASTA format.

FASTA is a plain-text file format like:

    >dengue_virus_seq1
    AGTTGAGATCTGTGT...

This step can be replaced with a FASTA file of any unknown virus.

### 🧪 Run BLAST to Compare Sequences
Uses BLAST (Basic Local Alignment Search Tool) to compare your viral sequence against thousands in NCBI's database. Each 'hit' is printed.

This helps identify similar viruses, strains, or organisms.

### 🧪 Parse and Summarize BLAST Hits
Parses XML results from NCBI BLAST and extracts:
* Top matching organisms
* Sequence similarity scores (bit scores, e-values)
* Aligned sequence regions
This helps process the BLAST hits.

### 🧪 Perform Multiple Sequence Alignment (MSA) with ClustalW
Aligns multiple viral genome sequences to highlight shared or differing regions.
This helps uncover conserved genetic patterns and mutations.

Aligning example:

    Sequence A: ATTGCCAGT
    Sequence B: ATTACCAGC
                ↑↑↑ ↑↑↑↑

### 🧪 Build and Visualize Phylogenetic Trees
Converts the alignment into a tree diagram showing how related the viruses are. The tree is built using the Newick format and rendered with Biopython’s Phylo module.

Example Tree:
<img src="https://openbooks.lib.msu.edu/app/uploads/sites/72/h5p/content/88/images/image-5efe3c6f9ed7b.gif" alt="Phylogenetic tree example" width="500"/>

Virus Phylogenetic Trees can tell help:

* Track virus evolution or mutation hotspots
* Distinguish between outbreak strains
* Choose representative sequences for vaccine or diagnostic design

### Modules
All steps are modularized in the ``src/`` directory making it easy to use and resue individual steps and swap in original data.

    ├── fetch_sequences.py
    ├── run_blast.py
    ├── align_and_tree.py
    └── utils.py

After each step, files like ``.fasta``, ``.xml``, ``.aln``, and ``.dnd`` can be downloaded.

## 🧬 Let's test the code!
Link to Colab notebook: [dengue_analysis.ipynb](https://colab.research.google.com/drive/1ZVyDpIpl_gsuaPH7dfulFxvbGQLWKHmf?usp=sharing)
A Jupyter notebook with the main script is available under ``notebooks/``.
The downloaded files from the example notebook are available under ``results/`` and ``data/``.

## 🧬 Project Installation
1. Clone this repository:

``git clone https://github.com/apoorvabr314/FinalProject_GLY4930_ABR.git
  cd virus-genomics``

2. Install dependencies:

``pip install -r requirements.txt``

3. [ClustalW2](http://www.clustal.org/clustal2/) must be installed separately to enable multiple sequence alignment. (It is not a python package but a seperate command-line tool.) 

On Ubuntu/Debian: ``sudo apt-get install clustalw``
On Mac (via Homebrew): ``brew install clustal-w``
On Colab: ``!apt-get install clustalw``.

## 🧬 Contributors
Project by Apoorva Bangalore Raviprasad.

## 🧬 Datasets
The demo uses Dengue Virus sequences dataset from the National Center for Biotechnology Information (NCBI) database.

- NCBI Virus Resource: Hatcher et al., 2017. [DOI: 10.1093/nar/gkw1065](https://doi.org/10.1093/nar/gkw1065)
- GenBank: Sayers et al., 2022. [DOI: 10.1093/nar/gkab1030](https://doi.org/10.1093/nar/gkab1030)
