def to_rna(dna_strand):
    rna = {'A':'U', 'C':'G', 'G':'C','T':'A'}
    return "".join(rna[char] for char in dna_strand)
